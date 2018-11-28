#include <iostream>
#include <string>

using namespace std;

int cas, CITY, xx;
int D[256], S[256];
int mapp[256][256];
double dist[256][256];

int main() {
  cin>>cas;
  for (int k=1; k<=cas; ++k) {
    cin>>CITY>>xx;
    for (int i=1; i<=CITY; ++i)
      cin>>D[i]>>S[i];
    for (int i=1; i<=CITY; ++i)
    for (int j=1; j<=CITY; ++j) {
      cin>>mapp[i][j];
      dist[i][j]=-1;
    }
    cin>>xx; cin>>xx;
    for (int i=1; i<=CITY; ++i) {
      int total_dis=0;
      for (int j=i+1; j<=CITY; ++j) {
        total_dis += mapp[j-1][j];
        if (total_dis<=D[i]) {
          dist[i][j]=(double)total_dis/S[i];
        }
        else break;
      }
    }

  //  for (int i=1; i<=CITY; ++i) {
  //    for (int j=1; j<=CITY; ++j)
  //      cout<<dist[i][j]<<" ";
  //    cout<<endl;
  //  }

    int update=1;
    while (update) {
      update=0;
      for (int i=1; i<=CITY; ++i)
      for (int j=1; j<=CITY; ++j)
      for (int m=1; m<=CITY; ++m)
        if (dist[i][j]>0 && dist[j][m]>0) {
          double txx = dist[i][j] + dist[j][m];
          if (dist[i][m]<0 || dist[i][m]>txx)
            {dist[i][m]=txx; ++update;}
        }
    }

  //  for (int i=1; i<=CITY; ++i) {
  //    for (int j=1; j<=CITY; ++j)
  //      cout<<dist[i][j]<<" ";
  //    cout<<endl;
  //  }

    cout<<"Case #"<<k<<": "<<dist[1][CITY]<<endl;
  }
  return 0;
}
