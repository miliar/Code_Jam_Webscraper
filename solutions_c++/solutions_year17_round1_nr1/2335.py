#include <bits/stdc++.h>
using namespace std;
pair<int,int>p[30];
int main()
{
	int a,r,c,k,f,b=1;
	char m[30][30];
	cin>>a;
	while(a--){
		k=0;
		for(int q=0;q<30;++q)
			for(int w=0;w<30;++w)m[q][w]='.';
		cin>>r>>c;
		for(int q=0;q<r;++q)
			for(int w=0;w<c;++w){
				cin>>m[q][w];
				if(m[q][w]!='?'){
					p[k].first=q;
					p[k].second=w;
					k++;
				}
			}
		sort(p,p+k);
		for(int q=0;q<k;++q){
			for(int w=p[q].second-1;w>=0;--w){
				if(m[p[q].first][w]=='?')m[p[q].first][w]=m[p[q].first][p[q].second];
				else break;
			}
			for(int w=p[q].second+1;w<c;++w){
				if(m[p[q].first][w]=='?')m[p[q].first][w]=m[p[q].first][p[q].second];
				else break;
			}
		}
		for(int q=0;q<r;++q){
			if(m[q][0]!='?'){
				for(int w=q-1;w>=0;--w){
					if(m[w][0]!='?')break;
					for(int e=0;e<c;++e)m[w][e]=m[q][e];
				}
				for(int w=q+1;w<r;++w){
					if(m[w][0]!='?')break;
					for(int e=0;e<c;++e)m[w][e]=m[q][e];
				}
			}
		}
		cout<<"Case #"<<b++<<":"<<endl;
		for(int q=0;q<r;++q){
			for(int w=0;w<c;++w)
				cout<<m[q][w];
			cout<<endl;
		}
	}
	return 0;
}

