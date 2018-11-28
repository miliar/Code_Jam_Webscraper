#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;

#define MAX_N 1000005

int T;
int R,C;
bitset<50> u;

struct str{
	char st[50];
}s[50];


int main(){
	freopen("A-large.in","r",stdin);
	freopen("ansA2.txt","w",stdout);

	scanf("%d",&T);
	

	for(int ts=1;ts<=T;++ts){
		scanf("%d%d",&R,&C);
		for(int i=1;i<=R;++i){
			scanf("%s",s[i].st+1);
		}
		u.reset();
		for(int i=1;i<=R;++i){
			bool jizz=true;
			for(int j=1;j<=C;++j){
				if(s[i].st[j]=='?')continue;
				else {
					jizz=false;
					break;
				}

			}
			if(jizz)u[i]=1;
		}
		bool up=false;

		for(int i=1;i<=R;++i){
			if(u[i]==1){
				if(!up)continue;
				
				for(int j=1;j<=C;++j){
					s[i].st[j]=s[i-1].st[j];
				}
			}
			else {
				bool check=false;
				for(int j=1;j<=C;++j){
					if(s[i].st[j]=='?' && !check)continue;
					if(s[i].st[j]!='?'){
						if(!check){
							for(int k=j-1;k>=1;--k){
								s[i].st[k]=s[i].st[j];
							}
							check=true;
							int j2=j;
							for(int k=j+1;k<=C;++k){
								if(s[i].st[k]!='?')break;
								s[i].st[k]=s[i].st[j];
								j2=k;
							}
							j=j2;
						}
						else {
							int j2=j;
							for(int k=j+1;k<=C;++k){
								if(s[i].st[k]!='?')break;
								s[i].st[k]=s[i].st[j];
								j2=k;
							}
							j=j2;
						}
					}
				}


				if(!up){
					for(int k=i-1;k>=1;--k){
						for(int j=1;j<=C;++j){
							s[k].st[j]=s[i].st[j];
						}
					}
					up=true;
				}
				//up=true;

			}
		}

		printf("Case #%d:\n",ts);
		for(int i=1;i<=R;++i){
			for(int j=1;j<=C;++j){
				putchar(s[i].st[j]);
			}
			puts("");
		}
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}
