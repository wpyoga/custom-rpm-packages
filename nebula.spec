Name:		nebula
Version:	1.6.0
Release:	2%{?dist}
Summary:	Nebula Mesh VPN

#Group:		
License:	MIT
URL:		https://github.com/slackhq/nebula

%undefine	_disable_source_fetch
%ifarch x86_64
Source0:	https://github.com/slackhq/%{name}/releases/download/v%{version}/%{name}-linux-amd64.tar.gz
%define		SHA256SUM0 f1a82c27624bf319c35f3bb4c136d5b82f26b014e8f5d16f64b3b0089f60220c
%endif
%ifarch aarch64
Source0:	https://github.com/slackhq/%{name}/releases/download/v%{version}/%{name}-linux-arm64.tar.gz
%define 	SHA256SUM0 40f926a8c86e2776259db5edf795b904dc8269c33b0d433f1c01e817d8368cd8
%endif

Source1:	https://github.com/slackhq/%{name}/raw/v%{version}/AUTHORS
%define		SHA256SUM1 2e0c79a5024c1ac2ea8752980bbd4ee8c53297abc583d72f315ad0b5bd4c2e26
Source2:	https://github.com/slackhq/%{name}/raw/v%{version}/CHANGELOG.md
%define		SHA256SUM2 da4a6f48fbe5ac8cdf652f6dc6a0625dd583ca52a5ad8357398e1d6980fe8b2e
Source3:	https://github.com/slackhq/%{name}/raw/v%{version}/LICENSE
%define		SHA256SUM3 aefd0cce553f24945ce1c692c3c4f9fda581f078ba82977845715cd18565b3bd
Source4:	https://github.com/slackhq/%{name}/raw/v%{version}/README.md
%define		SHA256SUM4 1f04b84a30932b4cc33dc9dad93dabeed757cc30b09be6dfb310922b82b24a79
Source5:	https://github.com/slackhq/%{name}/raw/v%{version}/examples/config.yml
%define		SHA256SUM5 4c3012a18618ad6b0447a0ff229ee59f59742defbd9bdffe956c95ce096a1dc1


#BuildArch:	x86_64
BuildRequires:	wget coreutils gzip tar
#Requires:	

%description
Nebula Mesh VPN tool.

%prep
echo %SHA256SUM0 %SOURCE0 | sha256sum -c -
echo %SHA256SUM1 %SOURCE1 | sha256sum -c -
echo %SHA256SUM2 %SOURCE2 | sha256sum -c -
echo %SHA256SUM3 %SOURCE3 | sha256sum -c -
echo %SHA256SUM4 %SOURCE4 | sha256sum -c -
echo %SHA256SUM5 %SOURCE5 | sha256sum -c -
gzip -dc %SOURCE0 | tar xv
cp %SOURCE0 .
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .


%build
# strip


%install
mkdir -p %{buildroot}/%{_bindir}
install -Dm 755 nebula %{buildroot}/%{_bindir}/nebula
install -Dm 755 nebula-cert %{buildroot}/%{_bindir}/nebula-cert
install -Dm 644 AUTHORS %{buildroot}/%{_docdir}/%{name}/AUTHORS
install -Dm 644 CHANGELOG.md %{buildroot}/%{_docdir}/%{name}/CHANGELOG.md
install -Dm 644 LICENSE %{buildroot}/%{_docdir}/%{name}/LICENSE
install -Dm 644 README.md %{buildroot}/%{_docdir}/%{name}/README.md
install -Dm 644 config.yml %{buildroot}/%{_docdir}/%{name}/examples/config.yml


%files
%{_bindir}/nebula
%{_bindir}/nebula-cert
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/examples/config.yml


%changelog

