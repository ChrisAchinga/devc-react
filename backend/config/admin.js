module.exports = ({ env }) => ({
  auth: {
    secret: env('ADMIN_JWT_SECRET', 'd77a24700449d2598e97aebac6a53afa'),
  },
});
