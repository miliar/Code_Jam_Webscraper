#include <bits/stdc++.h>
using namespace std;
int n,m;
vector<string>s;
int main(){
	int t,i,j,tc=0;
	cin >> t;
	while(t--){
		cin >> n >> m;
		s.resize(n);
		for(i=0;i<n;++i){
			cin >> s[i];
		}
		for(i=0;i<n;++i){
			for(j=0;s[i][j];++j){
				if(s[i][j]!='?'){
					if(s[i][j] != '?'){
					    for(int k= 0; k<m and (s[i][k] == '?' || s[i][k] == s[i][j] || k < j); k++){
					        if(k < j and s[i][k] == '?'){
					            s[i][k] = s[i][j];
					        }
					        else if(k > j and s[i][k] == '?'){
					            s[i][k] = s[i][j];
					        }
					    }
					}
				}
			}
		}
		for(i=0;i<n;++i){
			for(j=0;s[i][j];++j){
				if(s[i][j] != '?'){
				    for(int k = 0; k < n and (s[k][j] == '?' || s[k][j] == s[i][j] || k < i); k++){
				        if(k < i && s[k][j] == '?'){
				            s[k][j] = s[i][j];
				        }
				        else if(k > i && s[k][j] == '?'){
				            s[k][j] = s[i][j];
				        }
				    }
				}
			}
		}
		cout << "Case #" << ++tc << ":\n";
		for(i=0;i<n;++i)
		cout << s[i] << '\n';
	}
	return 0;
}