CREATE SEQUENCE public.users_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9999 START 1 CACHE 1;

CREATE TABLE "public"."users" (
    "id_user" integer DEFAULT nextval('public.users_id_seq') NOT NULL,
	"nombre" character varying(255) NOT NULL,
	"primer_apel" character varying(255) NOT NULL,
	"seg_apel" character varying(255) NOT NULL,
    "fec_nac" date NOT NULL,
    "created_at" timestamp(0),
    "updated_at" timestamp(0),
    CONSTRAINT "id_user_pkey" PRIMARY KEY ("id_user")
) WITH (oids = false);