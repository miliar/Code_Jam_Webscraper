#include <bits/stdc++.h>
#define N 32

using namespace std;
string tab[N];
int visited[N][N]={0};
int n,m,t;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int c=1;c<=t;++c) {
		cin>>n>>m;
		for(int i=0;i<n;++i) {
			cin>>tab[i];
		}
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				visited[i][j]=0;
		for(int i=0;i<n;++i) {
			int s = 0;
			int e=0;
			for(int j=0;j<m;++j) {
				if(tab[i][j]!='?' && !visited[i][j]) {

					int k;
					for(k=j+1;k<m;++k) {
						if(tab[i][k]!='?' || visited[i][k])
						{
							break;
						}
					}
					e = k;
					for(int k=s;k<e;++k) {
						tab[i][k]=tab[i][j];
						visited[i][k] = 1;
					}
					for(int p = i+1;p<n;++p) {
						bool check = true;
						for(int l = s; l<e;++l) {
							if(tab[p][l]!='?')
								check =false;
						}
						if(!check) break;
						for(int l=s;l<e;++l)
						{
							tab[p][l]=tab[i][j];
							visited[p][l]=1;
						}
					}
					for(int p=i-1;p>=0;--p) {
						bool check = true;
						for(int l = s; l<e;++l) {
							if(tab[p][l]!='?')
								check =false;
						}
						if(!check) break;
						for(int l=s;l<e;++l)
						{
							tab[p][l]=tab[i][j];
							visited[p][l]=1;
						}
					}
					
					s=e;
				} else if(visited[i][j]){
					s = j+1;
				}
			}
		}
		cout<<"Case #"<<c<<":"<<endl;
		for(int i=0;i<n;++i) {
			cout<<tab[i]<<endl;
		}
	}
}