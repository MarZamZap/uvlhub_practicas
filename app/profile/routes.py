from flask import request, render_template, flash, redirect, url_for
from flask_login import login_required

from app.profile import profile_bp
from app.profile.forms import UserProfileForm

from .models import UserProfile
from .. import get_authenticated_user_profile


@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UserProfileForm()

    if request.method == 'POST' and form.validate_on_submit():
        orcid = form.orcid.data
        name = form.name.data
        surname = form.surname.data

        profile = get_authenticated_user_profile()
        profile.orcid = orcid
        profile.name = name
        profile.surname = surname
        profile.save()

        flash('Saved profile', 'success')

        return render_template('profile/edit.html', form=form)

    else:
        return render_template('profile/edit.html', form=form)