#include <bits/stdc++.h>
using namespace std;
pair<int,int> pos[30];
int cake[30][30];
int result[30][30];
int r,c;

void fill(int now){
	int x=pos[now].first;
	int y=pos[now].second;
	if(!result[x][y]){
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				result[i][j]=now;
			}
		}
		return;
	}
	int pre=result[x][y];
	int px=pos[pre].first;
	int py=pos[pre].second;
	int minx=x,miny=y,maxx=x,maxy=y;
	while(result[minx][y]==pre) minx--;
	while(result[maxx][y]==pre) maxx++;
	while(result[x][miny]==pre) miny--;
	while(result[x][maxy]==pre) maxy++;
	minx++;
	maxx--;
	miny++;
	maxy--;
	if(x!=px){
		if(x<px){
			for(int i=minx;i<px;i++){
				for(int j=miny;j<=maxy;j++){
					result[i][j]=now;
				}
			}
			return;
		}
		else{
			for(int i=px+1;i<=maxx;i++){
				for(int j=miny;j<=maxy;j++){
					result[i][j]=now;
				}
			}
			return;
		}
	}
	if(y<py){
		for(int i=minx;i<=maxx;i++){
			for(int j=miny;j<py;j++){
				result[i][j]=now;
			}
		}
		return;
	}
	else{
		for(int i=minx;i<=maxx;i++){
			for(int j=py+1;j<=maxy;j++){
				result[i][j]=now;
			}
		}
		return;
	}


}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("Alarge.out","w",stdout);
	int T;
	cin>>T;

	for(int t=1;t<=T;t++){
		cin>>r>>c;
		for(int i=1;i<=26;i++){
			pos[i].first=0;
			pos[i].second=0;
		}
		memset(cake,0,sizeof(cake));
		memset(result,0,sizeof(result));
		for(int i=1;i<=r;i++){
			string s;
			cin>>s;
			for(int j=0;j<s.size();j++){
				if(s[j]=='?') cake[i][j+1]=0;
				else{
					cake[i][j+1]=s[j]-'A'+1;
					pos[s[j]-'A'+1].first=i;
					pos[s[j]-'A'+1].second=j+1;
				} 
			}
		}
		for(int i=1;i<=26;i++){
			if(pos[i].first) fill(i);
		}
		printf("Case #%d:\n",t);
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				cout<<(char)('A'+result[i][j]-1);
			}
			cout<<endl;
		}
	}
}
