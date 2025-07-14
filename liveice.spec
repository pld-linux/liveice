Summary:	Live audio streaming program
Summary(pl.UTF-8):	Program do streamingu audio na żywo
Name:		liveice
#		Set Date as Version
Version:	000530
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://star.arm.ac.uk/~spm/software/%{name}.tar.gz
# Source0-md5:	6b1c9c98225757c26f91083b233da0ff
Patch0:		%{name}-conf.patch
URL:		http://star.arm.ac.uk/~spm/software/liveice.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiveIce is a live streaming program that allows input either from your
soundcard's line in or from MP3 files to be mixed and re-encoded and
then streamed to an icecast server. This means that you can use
liveice with your microphone and do live audio broadcasts, or even use
a MP3 playlist and use the multi channel support to speed up, slow
down, adjust volumes, and mix between the two channels, and then
re-encode the data at a lower bitrate to be sent out to a icecast
server.

%description -l pl.UTF-8
LiveIce to program do streamingu na żywo, który pozwala miksować
sygnały audio z karty dźwiękowej, plików MP3. Przetworzony strumień
danych jest przesyłany do serwera icecast. To oznacza, że możesz
używać liveice z mikrofonem by tworzyć i nadawać audycje audio.

%prep
%setup -q -n %{name}
%patch -P0 -p1

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/icecast/%{name}.cfg
