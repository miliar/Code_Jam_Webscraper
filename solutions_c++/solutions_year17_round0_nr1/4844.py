#include<bits/stdc++.h>
using namespace std;




int main()
{
		freopen("A-large.in","r",stdin);
		freopen("A_large.out","w",stdout);
		int T,cas=0;
		scanf("%d",&T);
		string s;
		while(T--){
			bool t=1;
			int K;
			cin>>s>>K;
			int cnt=0;
			for(int i=0;i<s.size();i++){
				if(s[i]=='-'){
					if(i+K>s.size()){
						t=0;
						break;
					}
					for(int j=i,k=0;k<K;j++,k++){
						if(s[j]=='-')s[j]='+';
						else s[j]='-';
					}
					cnt++;
				}
			}
			if(!t)printf("Case #%d: IMPOSSIBLE\n", ++cas);
			else printf("Case #%d: %d\n", ++cas, cnt);
		}
		return 0;
}
