#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[])
{
	int N;
	while(cin>>N){
		for(int k=1; k<=N; k++){
			int a[7];
			string c = "0ROYGBV";
			string ans = "1";
			for(int i=0; i<7; i++) cin>>a[i];
			int index = 0;
			bool put = true;
			for(int i=1; i<7; i++){
				if(a[i] > a[0]/2) put = false;
			}
			while(index < a[0] && put){
				put = false;
				for(int i=1; i<6; i++){
					for(int j=i+1; j<7; j++){
						if(a[i]<a[j] || (a[i]==a[j]&&ans.size()!=1&&c[i]!=ans[1])){
							char t = c[i];
							c[i] = c[j];
							c[j] = t;
							int tt = a[i];
							a[i] = a[j];
							a[j] = tt;
						}
					}
				}
				for(int i=1; i<7&&!put; i++){
					if(ans[index] != c[i]){
						ans += c[i];
						put = true;
						a[i]--;
						index++;
					}
				}
			}
			cout<<"Case #"<<k<<": ";
			if(put && ans[1] != ans[a[0]]){
				for(int i=1; i<ans.size(); i++) cout<<ans[i];
				cout<<endl;
			}
			else cout<<"IMPOSSIBLE\n";
		}
	}
    return 0;
}
