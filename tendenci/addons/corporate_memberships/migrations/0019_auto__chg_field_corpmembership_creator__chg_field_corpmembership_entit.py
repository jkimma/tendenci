# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CorpMembership.creator'
        db.alter_column('corporate_memberships_corpmembership', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpMembership.entity'
        db.alter_column('corporate_memberships_corpmembership', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorpMembership.owner'
        db.alter_column('corporate_memberships_corpmembership', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpMembershipImport.creator'
        db.alter_column('corporate_memberships_corpmembershipimport', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'CorpProfile.creator'
        db.alter_column('corporate_memberships_corpprofile', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpProfile.entity'
        db.alter_column('corporate_memberships_corpprofile', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorpProfile.owner'
        db.alter_column('corporate_memberships_corpprofile', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.creator'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.entity'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorporateMembershipArchive.owner'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.approved_denied_user'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'approved_denied_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'CorporateMembershipArchive.archive_user'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'archive_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'IndivMembEmailVeri8n.updated_by'
        db.alter_column('corporate_memberships_indivmembemailveri8n', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'IndivMembEmailVeri8n.creator'
        db.alter_column('corporate_memberships_indivmembemailveri8n', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpMembershipApp.creator'
        db.alter_column('corporate_memberships_corpmembershipapp', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpMembershipApp.entity'
        db.alter_column('corporate_memberships_corpmembershipapp', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorpMembershipApp.owner'
        db.alter_column('corporate_memberships_corpmembershipapp', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpApp.creator'
        db.alter_column('corporate_memberships_corpapp', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpApp.entity'
        db.alter_column('corporate_memberships_corpapp', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorpApp.owner'
        db.alter_column('corporate_memberships_corpapp', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorpMembRenewEntry.creator'
        db.alter_column('corporate_memberships_corpmembrenewentry', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'CorporateMembershipType.creator'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembershipType.entity'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorporateMembershipType.owner'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'Notice.owner'
        db.alter_column('corporate_memberships_notice', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'Notice.creator'
        db.alter_column('corporate_memberships_notice', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembership.creator'
        db.alter_column('corporate_memberships_corporatemembership', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembership.entity'
        db.alter_column('corporate_memberships_corporatemembership', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['entities.Entity'], null=True))

        # Changing field 'CorporateMembership.owner'
        db.alter_column('corporate_memberships_corporatemembership', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'CorporateMembership.approved_denied_user'
        db.alter_column('corporate_memberships_corporatemembership', 'approved_denied_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'IndivEmailVerification.updated_by'
        db.alter_column('corporate_memberships_indivemailverification', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'IndivEmailVerification.creator'
        db.alter_column('corporate_memberships_indivemailverification', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

    def backwards(self, orm):

        # Changing field 'CorpMembership.creator'
        db.alter_column('corporate_memberships_corpmembership', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpMembership.entity'
        db.alter_column('corporate_memberships_corpmembership', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorpMembership.owner'
        db.alter_column('corporate_memberships_corpmembership', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpMembershipImport.creator'
        db.alter_column('corporate_memberships_corpmembershipimport', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'CorpProfile.creator'
        db.alter_column('corporate_memberships_corpprofile', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpProfile.entity'
        db.alter_column('corporate_memberships_corpprofile', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorpProfile.owner'
        db.alter_column('corporate_memberships_corpprofile', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.creator'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.entity'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorporateMembershipArchive.owner'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembershipArchive.approved_denied_user'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'approved_denied_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'CorporateMembershipArchive.archive_user'
        db.alter_column('corporate_memberships_corporatemembershiparchive', 'archive_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'IndivMembEmailVeri8n.updated_by'
        db.alter_column('corporate_memberships_indivmembemailveri8n', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'IndivMembEmailVeri8n.creator'
        db.alter_column('corporate_memberships_indivmembemailveri8n', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpMembershipApp.creator'
        db.alter_column('corporate_memberships_corpmembershipapp', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpMembershipApp.entity'
        db.alter_column('corporate_memberships_corpmembershipapp', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorpMembershipApp.owner'
        db.alter_column('corporate_memberships_corpmembershipapp', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpApp.creator'
        db.alter_column('corporate_memberships_corpapp', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpApp.entity'
        db.alter_column('corporate_memberships_corpapp', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorpApp.owner'
        db.alter_column('corporate_memberships_corpapp', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorpMembRenewEntry.creator'
        db.alter_column('corporate_memberships_corpmembrenewentry', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'CorporateMembershipType.creator'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembershipType.entity'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorporateMembershipType.owner'
        db.alter_column('corporate_memberships_corporatemembershiptype', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'Notice.owner'
        db.alter_column('corporate_memberships_notice', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'Notice.creator'
        db.alter_column('corporate_memberships_notice', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembership.creator'
        db.alter_column('corporate_memberships_corporatemembership', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembership.entity'
        db.alter_column('corporate_memberships_corporatemembership', 'entity_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['entities.Entity']))

        # Changing field 'CorporateMembership.owner'
        db.alter_column('corporate_memberships_corporatemembership', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'CorporateMembership.approved_denied_user'
        db.alter_column('corporate_memberships_corporatemembership', 'approved_denied_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'IndivEmailVerification.updated_by'
        db.alter_column('corporate_memberships_indivemailverification', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'IndivEmailVerification.creator'
        db.alter_column('corporate_memberships_indivemailverification', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'categories.categoryitem': {
            'Meta': {'object_name': 'CategoryItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'categoryitem_category'", 'null': 'True', 'to': "orm['categories.Category']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'categoryitem_parent'", 'null': 'True', 'to': "orm['categories.Category']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'corporate_memberships.authorizeddomain': {
            'Meta': {'object_name': 'AuthorizedDomain'},
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_domains'", 'to': "orm['corporate_memberships.CorporateMembership']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'corporate_memberships.corpapp': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CorpApp'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authentication_method': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'confirmation_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corp_memb_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['corporate_memberships.CorporateMembershipType']", 'symmetrical': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpapp_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corpapp_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memb_app': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'corp_app'", 'unique': 'True', 'to': "orm['memberships.App']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpapp_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['payments.PaymentMethod']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '155'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corpfield': {
            'Meta': {'object_name': 'CorpField'},
            'admin_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'corp_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['corporate_memberships.CorpApp']"}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'field_layout': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'default': "'CharField'", 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'no_duplicates': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'corporate_memberships.corpfieldentry': {
            'Meta': {'object_name': 'CorpFieldEntry'},
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['corporate_memberships.CorporateMembership']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'field'", 'to': "orm['corporate_memberships.CorpField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        'corporate_memberships.corpmembership': {
            'Meta': {'object_name': 'CorpMembership'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anonymous_creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.Creator']", 'null': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approved_denied_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'approved_denied_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'corp_profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corp_memberships'", 'to': "orm['corporate_memberships.CorpProfile']"}),
            'corporate_membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembershipType']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpmembership_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corpmembership_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expiration_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'join_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpmembership_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['payments.PaymentMethod']", 'null': 'True'}),
            'renew_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corpmembershipapp': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CorpMembershipApp'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authentication_method': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'confirmation_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corp_memb_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['corporate_memberships.CorporateMembershipType']", 'symmetrical': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpmembershipapp_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corpmembershipapp_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memb_app': ('django.db.models.fields.related.OneToOneField', [], {'default': '1', 'related_name': "'corp_app'", 'unique': 'True', 'to': "orm['memberships.MembershipApp']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpmembershipapp_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['payments.PaymentMethod']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '155'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corpmembershipappfield': {
            'Meta': {'ordering': "('position',)", 'object_name': 'CorpMembershipAppField'},
            'admin_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'corp_app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['corporate_memberships.CorpMembershipApp']"}),
            'css_class': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'field_layout': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'default': "'CharField'", 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corpmembershipauthdomain': {
            'Meta': {'object_name': 'CorpMembershipAuthDomain'},
            'corp_profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authorized_domains'", 'to': "orm['corporate_memberships.CorpProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'corporate_memberships.corpmembershipimport': {
            'Meta': {'object_name': 'CorpMembershipImport'},
            'bind_members': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'complete_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '50'}),
            'num_processed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'override': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not_started'", 'max_length': '50'}),
            'summary': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True'}),
            'total_rows': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'max_length': '260'})
        },
        'corporate_memberships.corpmembershipimportdata': {
            'Meta': {'object_name': 'CorpMembershipImportData'},
            'action_taken': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimport': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corp_membership_import_data'", 'to': "orm['corporate_memberships.CorpMembershipImport']"}),
            'row_data': ('tendenci.core.base.fields.DictField', [], {}),
            'row_num': ('django.db.models.fields.IntegerField', [], {})
        },
        'corporate_memberships.corpmembershiprep': {
            'Meta': {'unique_together': "(('corp_profile', 'user'),)", 'object_name': 'CorpMembershipRep'},
            'corp_profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reps'", 'to': "orm['corporate_memberships.CorpProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dues_rep': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_member_rep': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'corporate_memberships.corpmembrenewentry': {
            'Meta': {'object_name': 'CorpMembRenewEntry'},
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembership']"}),
            'corporate_membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembershipType']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'corporate_memberships.corporatemembership': {
            'Meta': {'object_name': 'CorporateMembership'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anonymous_creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.Creator']", 'null': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approved_denied_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'approved_denied_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'corp_app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorpApp']"}),
            'corporate_membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembershipType']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembership_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corporatemembership_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expiration_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'join_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembership_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['payments.PaymentMethod']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'renew_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'renew_entry_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corporatemembershiparchive': {
            'Meta': {'object_name': 'CorporateMembershipArchive'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approved_denied_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'approved_denied_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'archive_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corp_memb_archiver'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'corp_memb_create_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'corp_memb_update_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembership']"}),
            'corporate_membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembershipType']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembershiparchive_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corporatemembershiparchive_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expiration_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'join_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembershiparchive_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['payments.PaymentMethod']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'renew_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'renew_entry_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corporatemembershiprep': {
            'Meta': {'unique_together': "(('corporate_membership', 'user'),)", 'object_name': 'CorporateMembershipRep'},
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reps'", 'to': "orm['corporate_memberships.CorporateMembership']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dues_rep': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_member_rep': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'corporate_memberships.corporatemembershiptype': {
            'Meta': {'ordering': "('position',)", 'object_name': 'CorporateMembershipType'},
            'admin_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apply_threshold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembershiptype_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corporatemembershiptype_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual_threshold': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'individual_threshold_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipType']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corporatemembershiptype_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'renewal_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'corporate_memberships.corpprofile': {
            'Meta': {'object_name': 'CorpProfile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'annual_ad_expenditure': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'annual_revenue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'chapter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpprofile_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_memberships_corpprofile_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expectations': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['industries.Industry']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'number_employees': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'corporate_memberships_corpprofile_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'referral_source': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'referral_source_member_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'referral_source_member_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'referral_source_other': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['regions.Region']", 'null': 'True', 'blank': 'True'}),
            'secret_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ud1': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud2': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud3': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud4': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud5': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud6': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud7': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ud8': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        'corporate_memberships.creator': {
            'Meta': {'object_name': 'Creator'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'corporate_memberships.indivemailverification': {
            'Meta': {'object_name': 'IndivEmailVerification'},
            'corp_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorpProfile']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corp_email_veri8n_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corp_email_veri8n_updator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'verified_email': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'corporate_memberships.indivmembemailveri8n': {
            'Meta': {'object_name': 'IndivMembEmailVeri8n'},
            'corporate_membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembership']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ime_veri8n_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ime_veri8n_updator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'verified_email': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'corporate_memberships.indivmembershiprenewentry': {
            'Meta': {'object_name': 'IndivMembershipRenewEntry'},
            'corp_membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorpMembership']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipDefault']"}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'})
        },
        'corporate_memberships.indivmembrenewentry': {
            'Meta': {'object_name': 'IndivMembRenewEntry'},
            'corp_memb_renew_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorpMembRenewEntry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.Membership']"})
        },
        'corporate_memberships.notice': {
            'Meta': {'object_name': 'Notice'},
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '10'}),
            'corporate_membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corporate_memberships.CorporateMembershipType']", 'null': 'True', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_membership_notice_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email_content': ('tinymce.models.HTMLField', [], {}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notice_time': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'notice_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'num_days': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'corporate_membership_notice_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sender_display': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'system_generated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'corporate_memberships.noticelog': {
            'Meta': {'object_name': 'NoticeLog'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['corporate_memberships.Notice']"}),
            'notice_sent_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'num_sent': ('django.db.models.fields.IntegerField', [], {})
        },
        'corporate_memberships.noticelogrecord': {
            'Meta': {'object_name': 'NoticeLogRecord'},
            'action_taken': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'action_taken_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'corp_membership': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log_records'", 'to': "orm['corporate_memberships.CorpMembership']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice_log': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log_records'", 'to': "orm['corporate_memberships.NoticeLog']"})
        },
        'directories.directory': {
            'Meta': {'object_name': 'Directory'},
            'activation_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('tinymce.models.HTMLField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'directories_directory_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'design_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'enclosure_length': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'enclosure_type': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'enclosure_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'directories_directory_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expiration_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'list_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '260', 'blank': 'True'}),
            'meta': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['meta.Meta']", 'unique': 'True', 'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'directories_directory_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pricing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directories.DirectoryPricing']", 'null': 'True'}),
            'renewal_notice_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'requested_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('tendenci.core.base.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'syndicate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'timezone': ('timezones.fields.TimeZoneField', [], {'default': "'America/Chicago'", 'max_length': '100'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'directories.directorypricing': {
            'Meta': {'object_name': 'DirectoryPricing'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'directory_pricing_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'directory_pricing_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'premium_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'premium_price_member': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'regular_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'regular_price_member': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'show_member_pricing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'entities.entity': {
            'Meta': {'ordering': "('entity_name',)", 'object_name': 'Entity'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'entity_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'entity_parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'entity_children'", 'null': 'True', 'to': "orm['entities.Entity']"}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'industries.industry': {
            'Meta': {'object_name': 'Industry'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'industries_industry_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'industries_industry_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'industry_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'industries_industry_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'invoices.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'arrival_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'bill_to': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'bill_to_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'bill_to_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_to_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_to_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_to_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_to_fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_to_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_to_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_to_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_to_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_to_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'box_and_packing': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoice_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'disclaimer': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'discount_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'discount_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'estimate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gift': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'greeting': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoice_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'payments_credits': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'po': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'receipt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ship_date': ('django.db.models.fields.DateTimeField', [], {}),
            'ship_to': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'ship_to_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'ship_to_address_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ship_to_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_to_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ship_to_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_to_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ship_to_fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ship_to_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_to_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_to_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ship_to_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_to_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ship_via': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'shipping': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'shipping_surcharge': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'estimate'", 'max_length': '50'}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '4'}),
            'tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tax_exemptid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tax_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'taxable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tender_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'terms': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'variance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '4'}),
            'variance_notes': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        'memberships.app': {
            'Meta': {'object_name': 'App'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'confirmation_text': ('tinymce.models.HTMLField', [], {}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_app_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships_app_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['memberships.MembershipType']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_app_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['payments.PaymentMethod']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'use_captcha': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_corp': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'memberships.membership': {
            'Meta': {'object_name': 'Membership'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'corporate_membership_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membership_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships_membership_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expire_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']", 'null': 'True', 'blank': 'True'}),
            'ma': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.App']", 'null': 'True'}),
            'member_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membership_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['payments.PaymentMethod']", 'null': 'True', 'blank': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_notice': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'subscribe_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': "orm['auth.User']"})
        },
        'memberships.membershipapp': {
            'Meta': {'object_name': 'MembershipApp'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_multiple_membership': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'confirmation_text': ('tinymce.models.HTMLField', [], {}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershipapp_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discount_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships_membershipapp_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['memberships.MembershipType']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershipapp_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['payments.PaymentMethod']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'use_captcha': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_corp': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'memberships.membershipdefault': {
            'Meta': {'object_name': 'MembershipDefault'},
            'action_taken': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'action_taken_dt': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'action_taken_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'action_taken_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'affiliation_member_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipApp']", 'null': 'True'}),
            'application_abandoned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'application_abandoned_dt': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'application_abandoned_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_abandond_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'application_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'application_approved_denied_dt': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'application_approved_denied_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_approved_denied_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'application_approved_dt': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'application_approved_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_approved_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'application_complete': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'application_complete_dt': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'application_complete_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_complete_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'application_denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'areas_of_expertise': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'bod_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'certifications': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'chapter': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'company_size': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'corp_profile_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'corporate_membership_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershipdefault_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'directory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directories.Directory']", 'null': 'True', 'blank': 'True'}),
            'directory_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships_membershipdefault_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expire_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'exported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'government_agency': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '250', 'blank': 'True'}),
            'government_worker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['user_groups.Group']", 'null': 'True', 'symmetrical': 'False'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'home_state': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'how_long_in_practice': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['industries.Industry']", 'null': 'True', 'blank': 'True'}),
            'join_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'eng'", 'max_length': '10'}),
            'license_number': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'license_state': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'member_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'membership_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipSet']", 'null': 'True', 'blank': 'True'}),
            'membership_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.MembershipType']"}),
            'network_sectors': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '250', 'blank': 'True'}),
            'networking': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '250', 'blank': 'True'}),
            'newsletter_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'override_price': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershipdefault_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['payments.PaymentMethod']", 'null': 'True'}),
            'payment_received_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'personnel_notified_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'primary_practice': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'promotion_code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'referer_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'referral_source': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'referral_source_member_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'referral_source_member_number': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'referral_source_other': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['regions.Region']", 'null': 'True', 'blank': 'True'}),
            'renew_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'work_experience': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'year_left_native_country': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'memberships.membershipset': {
            'Meta': {'object_name': 'MembershipSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"})
        },
        'memberships.membershiptype': {
            'Meta': {'object_name': 'MembershipType'},
            'admin_fee': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'admin_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_renewal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershiptype_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships_membershiptype_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'expiration_grace_period': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fixed_option1_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option1_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option1_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option2_can_rollover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fixed_option2_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option2_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_option2_rollover_days': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membership_types'", 'to': "orm['user_groups.Group']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'never_expires': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'memberships_membershiptype_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'period': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'period_type': ('django.db.models.fields.CharField', [], {'default': "'rolling'", 'max_length': '10'}),
            'period_unit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'renewal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'renewal_period_end': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'renewal_period_start': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'renewal_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'renewal_require_approval': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'require_approval': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'require_payment_approval': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rolling_option': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rolling_option1_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rolling_renew_option': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rolling_renew_option1_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rolling_renew_option2_day': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'meta.meta': {
            'Meta': {'object_name': 'Meta'},
            'canonical_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'payments.paymentmethod': {
            'Meta': {'object_name': 'PaymentMethod'},
            'admin_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'perms.objectpermission': {
            'Meta': {'object_name': 'ObjectPermission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_groups.Group']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'regions.region': {
            'Meta': {'object_name': 'Region'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'regions_region_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regions_region_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'regions_region_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region_code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'user_groups.group': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Group'},
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_self_add': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_self_remove': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_respond': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_respond_priority': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'user_groups_group_creator'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_recipient': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_groups_group_entity'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['entities.Entity']", 'blank': 'True', 'null': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': "orm['auth.Group']", 'unique': 'True', 'null': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['user_groups.GroupMembership']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'user_groups_group_owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_permissions'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'show_as_option': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('tendenci.core.base.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'sync_newsletters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'distribution'", 'max_length': '75', 'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'user_groups.groupmembership': {
            'Meta': {'unique_together': "(('group', 'member'),)", 'object_name': 'GroupMembership'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_member'", 'to': "orm['auth.User']"}),
            'owner_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['corporate_memberships']