#include <vector>
#include <sstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;


void main2(){
	int N,M;
	cin>>N>>M;
	
	vector<char> A(N*N);
	for(int m=0;m<M;m++){
		char a;
		int r,c;
		cin>>a>>r>>c;
		r--;c--;
		switch(a){
		case '.':
			A[r*N+c]=0;
			break;
		case '+':
			A[r*N+c]=1;
			break;
		case 'x':
			A[r*N+c]=2;
			break;
		case 'o':
			A[r*N+c]=3;
			break;
		}
	}
	vector<char> F(A);
	vector<char> COL(N,1);
	vector<char> ROW(N,1);
	for(int r=0;r<N;r++){
		for(int c=0;c<N;c++){
			if(A[r*N+c]&2){
				COL[c]=0;
				ROW[r]=0;
			}
		}
	}
	for(int r=0;r<N;r++){
		for(int c=0;c<N;c++){
			if(COL[c]&&ROW[r]){
				F[r*N+c]+=2;
				COL[c]=0;
				ROW[r]=0;
			}
		}
	}
	
	vector<char> SUM(2*N-1,1);
	vector<char> DIFF(2*N-1,1);
	for(int r=0;r<N;r++){
		for(int c=0;c<N;c++){
			if(A[r*N+c]&1){
				SUM[r+c]=0;
				DIFF[N-1+r-c]=0;
			}
		}
	}
	vector<pair<int,int>> sp;
	for(int s=0;s<2*N-1;s++){
		if(SUM[s]) sp.push_back(make_pair(min(s,2*N-2-s),s));
	}
	sort(sp.begin(),sp.end());
	vector<pair<int,int>> dp;
	for(int d=0;d<2*N-1;d++){
		if(DIFF[d]) dp.push_back(make_pair(min(d,2*N-2-d),d));
	}
	sort(dp.begin(),dp.end());
	for(auto s:sp){
		for(auto dit=dp.begin();dit!=dp.end();dit++){
			auto d=*dit;
			if((s.second+d.second-N+1)%2) continue;
			//cerr<<(s.second+d.second-N+1)<<','<<(s.second-d.second+N-1)<<endl;
			int r=(s.second+d.second-N+1)/2;
			int c=(s.second-d.second+N-1)/2;
			if(r>=0&&c>=0&&r<N&&c<N){
				F[r*N+c]+=1;
				dp.erase(dit);
				break;
			}
		}
	}
	

	vector<char> mchars{'.','+','x','o'};
	

	
	int count=0;
	int point=0;
	for(int n=0;n<N*N;n++){
		if(F[n]!=A[n])count++;
		point+=F[n]&1;
		point+=F[n]/2;
	}
	cout<<point<<' '<<count;
	for(int r=0;r<N;r++){
		for(int c=0;c<N;c++){
			if(F[r*N+c]!=A[r*N+c]) cout<<endl<<mchars[F[r*N+c]]<<' '<<r+1<<' '<<c+1;
		}
	}

	if(N<20){
		cerr<<endl;
		cerr<<N<<' '<<point<<' '<<count;
		for(int r=0;r<N;r++){
			cerr<<endl;
			for(int c=0;c<N;c++){
				cerr<<mchars[A[r*N+c]];
			}
		}
		cerr<<endl;
		for(int r=0;r<N;r++){
			cerr<<endl;
			for(int c=0;c<N;c++){
				cerr<<mchars[F[r*N+c]];
			}
		}
		cerr<<endl;
	}
}

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		main2();
		cout<<endl;
	}
}
