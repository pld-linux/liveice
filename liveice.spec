Summary:	live audio streaming program
Summary(pl):	Program do streamingu audio na ¿ywo
Name:		liveice
#		Set Date as Version
Version:	000530
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://star.arm.ac.uk/~spm/software/%{name}.tar.gz
Patch0:		%{name}-conf.patch
URL:		http://star.arm.ac.uk/~spm/software/liveice.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiveIce is a live streaming program that allows input either from your
soundcard's line in or from mp3 files to be mixed and re-encoded and
then streamed to an icecast server. This means that you can use
liveice with your microphone and do live audio broadcasts, or even use
a mp3 playlist and use the multi channel support to speed up, slow
down, adjust volumes, and mix between the two channels, and then
re-encode the data at a lower bitrate to be sent out to a icecast
server.

%description -l pl
LiveIce to program do streamingu na ¿ywo, który pozwala miksowaæ
sygna³y audio z karty d¼wiêkowej, plików mp3. Przetworzony strumieñ
danych jest przesy³any do serwera icecast. To oznacza, ¿e mo¿esz
u¿ywaæ liveice z mikrofonem by tworzyæ i nadawaæ audycje audio.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__autoheader}
%{__autoconf}
%configure \
	-enable-fsstd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/%{name}
%attr(750,root,root) %dir %{_sysconfdir}/icecast
%dir %{_var}/log/icecast
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/icecast/%{name}.cfg
