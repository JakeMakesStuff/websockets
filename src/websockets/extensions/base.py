"""
The :mod:`websockets.extensions.base` module defines abstract classes for
implementing extensions as specified in `section 9 of RFC 6455`_.

.. _section 9 of RFC 6455: http://tools.ietf.org/html/rfc6455#section-9

"""


class ClientExtensionFactory:
    """
    Abstract class for client-side extension factories.

    """

    @property
    def name(self):
        """
        Extension identifier.

        """

    def get_request_params(self):
        """
        Build request parameters.

        Return a list of (name, value) pairs.

        """

    def process_response_params(self, params, accepted_extensions):
        """
        Process response parameters received from the server.

        ``params`` is a list of (name, value) pairs.

        ``accepted_extensions`` is a list of previously accepted extensions.

        If parameters are acceptable, return an extension: an instance of a
        subclass of :class:`Extension`.

        If they aren't, raise :exc:`~websockets.exceptions.NegotiationError`.

        """


class ServerExtensionFactory:
    """
    Abstract class for server-side extension factories.

    """

    @property
    def name(self):
        """
        Extension identifier.

        """

    def process_request_params(self, params, accepted_extensions):
        """
        Process request parameters received from the client.

        ``params`` is a list of (name, value) pairs.

        ``accepted_extensions`` is a list of previously accepted extensions.

        To accept the offer, return a 2-uple containing:

        - response parameters: a list of (name, value) pairs
        - an extension: an instance of a subclass of :class:`Extension`

        To reject the offer, raise
        :exc:`~websockets.exceptions.NegotiationError`.

        """


class Extension:
    """
    Abstract class for extensions.

    """

    @property
    def name(self):
        """
        Extension identifier.

        """

    def decode(self, frame, *, max_size=None):
        """
        Decode an incoming frame.

        The ``frame`` parameter and the return value are
        :class:`~websockets.framing.Frame` instances.



        """

    def encode(self, frame):
        """
        Encode an outgoing frame.

        The ``frame`` parameter and the return value are
        :class:`~websockets.framing.Frame` instances.

        """
