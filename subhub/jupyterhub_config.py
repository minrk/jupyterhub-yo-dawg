# use generic oauth to authenticate with the hub
c.JupyterHub.authenticator_class = "generic-oauth"

# the text displayed on the login button
# "Sign in with ..."
c.GenericOAuthenticator.login_service = "your other JupyterHub"

# client id, secret match service definition
c.GenericOAuthenticator.client_id = "service-subhub"
# client secret matches service.api_token in hubhub config:
c.GenericOAuthenticator.client_secret = (
    "a95d06e5ae237384e172ead59209e86912b930939bb46ee56be1dda447d9dab4"
)

# the public URL of the hub
hubhub_url = "http://hubhub.local.minrk.net:8000"


# OAuth urls for jupyterhub, in order of request:

# 1. authorize is the redirect target to start OAuth
c.GenericOAuthenticator.authorize_url = f"{hubhub_url}/hub/api/oauth2/authorize"

# 2. after authorizing with 'hubhub', browser is redirected back to this callback url
# Setting oauth_callback_url is usually redundant, but let's be explicit
# OAuthenticator detects this based on the request host, so it's rarely needed
c.GenericOAuthenticator.oauth_callback_url = (
    "http://subhub.local.minrk.net:9000/hub/oauth_callback"
)

# 3. in the oauth callback handler, we make this request to complete OAuth
# and request the access token.
# This is a hub->hub API request, so might not always need to use the public hub URL
c.GenericOAuthenticator.token_url = f"{hubhub_url}/hub/api/oauth2/token"

# 4. after issuing the token, this request is made *with* the token
# to retrieve the user model
c.GenericOAuthenticator.userdata_url = f"{hubhub_url}/hub/api/user"

# GenericOAuthenticator's default is to send client id/secret in Basic auth header
# but jupyterhub's validator only accepts them in the POST params
# (It probably should!)
c.GenericOAuthenticator.basic_auth = False
c.GenericOAuthenticator.extra_params = {
    "client_id": c.GenericOAuthenticator.client_id,
    "client_secret": c.GenericOAuthenticator.client_secret,
}

# usernames are in the 'name' field of the user model
c.GenericOAuthenticator.username_key = "name"

# uninteresting testing boilerplate below
# mostly ports to avoid collision since we are running on the same host as hubhub
c.JupyterHub.bind_url = "http://127.0.0.1:9000"
c.ConfigurableHTTPProxy.api_url = "http://127.0.0.1:9001"
c.JupyterHub.hub_bind_url = "http://127.0.0.1:9091"
c.JupyterHub.spawner_class = "simple"

# debug logging
# c.JupyterHub.log_level = 10
