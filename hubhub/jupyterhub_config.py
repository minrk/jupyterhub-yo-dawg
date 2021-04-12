# register the 'subhub' as a service
c.JupyterHub.services = [
    {
        "name": "subhub",
        # redirect uri for OAuthenticator is "{hub_public_host}/hub/oauth_callback}"
        "oauth_redirect_uri": "http://subhub.local.minrk.net:9000/hub/oauth_callback",
        # oauth_client_id could be omitted, default is `service-$name`
        "oauth_client_id": "service-subhub",
        # api_token is the oauth client secret
        "api_token": "a95d06e5ae237384e172ead59209e86912b930939bb46ee56be1dda447d9dab4",
    },
]

# uninteresting testing boilerplate:
# this should be replaced with 'real' config

# dummy auth for the 'hub of hubs' for testing
c.JupyterHub.authenticator_class = "dummy"
# use 'simple' spawner for testing
c.JupyterHub.spawner_class = "simple"

# debug logging
# c.JupyterHub.log_level = 10
