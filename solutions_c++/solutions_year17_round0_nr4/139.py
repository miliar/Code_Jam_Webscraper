#include<iostream>
#include<vector>
#include<queue>


using namespace std;



vector<vector<int> > A, B;
vector<vector<int> > E;


int L;

vector<bool> u;


bool df(int a){
  if (a==L-1)
    return 1;
  u[a]=1;
  for (int i=0; i<L; ++i){
    if (!u[i] && E[a][i]){
      if (df(i)){
	E[a][i]=0;
	E[i][a]=1;
	return 1;
      }
    }
  }
  return 0;
}





int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    int N, M; cin>>N>>M;
    A=vector<vector<int> >(N,vector<int>(N,0));
    for (int k=0; k<M; ++k){
      char c; int i,j; cin>>c>>i>>j;
      --i; --j;
      if (c=='o')
	A[i][j]=3;
      if (c=='x')
	A[i][j]=2;
      if (c=='+')
	A[i][j]=1;
	
    }
    B=A;
    for (int i=0; i<N; ++i){
      for (int j=0; j<N; ++j){
	bool ja=1;
	for (int k=0; k<N; ++k)
	  if (A[i][k]&2)
	    ja=0;
	for (int k=0; k<N; ++k)
	  if (A[k][j]&2)
	    ja=0;
	if (ja)
	  A[i][j]^=2;
      }
    }
    L=N*4;
    E=vector<vector<int> >(L,vector<int>(L,0));
    for (int k=0; k<2*N-1; ++k)
      E[L-2][k]=1;
    for (int k=2*N-1; k<4*N-2;++k)
      E[k][L-1]=1;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j){
	if (!(A[i][j]&1)){
	  E[i+j][3*N-2+i-j]=1;
	}
	else{
	  E[L-2][i+j]=0;
	  E[3*N-2+i-j][L-1]=0;
	}
      }
    u=vector<bool>(L,0);
    while(df(L-2)){
      u=vector<bool>(L,0);
    }
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j)
	if (E[3*N-2+i-j][i+j])
	  A[i][j]^=1;
    int x=0;
    int y=0;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j){
	if (A[i][j]!=B[i][j])
	  ++y;
	x+=(A[i][j]&1)+!!(A[i][j]&2);
      }
    cout<<"Case #"<<tc<<": "<<x<<" "<<y<<endl;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j){
	if (A[i][j]!=B[i][j]){
	  if (A[i][j]==3)
	    cout<<"o ";
	  if (A[i][j]==2)
	    cout<<"x ";
	  if (A[i][j]==1)
	    cout<<"+ ";
	  cout<<i+1<<" "<<j+1<<endl;
	}
      }
    


  }
  return 0;
}
