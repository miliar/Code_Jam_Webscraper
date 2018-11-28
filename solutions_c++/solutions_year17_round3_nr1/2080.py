#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(void) {
int t, count =1;
    cin>>t;
    while(count <= t)
    {
                  int N,k ;
                  cin>>N>>k;
                  double A[N][2];

                    for(int i=0;i<N;i++)
                    {
                        cin>>A[i][0]>>A[i][1];
                    }

                  // vector<vector<int> > combinations;
                 vector<int> selected;
                 vector<int> selector(N);
                 fill(selector.begin(), selector.begin() + k, 1);
                 double max = -1.0;
                 do {
                     for (int i = 0; i < N; i++)
                      {
                        if (selector[i]) {
                            selected.push_back(i);
                      }
                     }
                    double sum = 0.0;
                     int len = selected.size(), maxr = -1;
                     for(int i=0;i<len;i++)
                     {
                        sum += A[selected[i]][0]* A[selected[i]][1];
                        if( A[selected[i]][0] > maxr)
                            maxr =  A[selected[i]][0];
                     }

                      sum = sum*2*3.14159265359;
                      sum += 3.14159265359*maxr*maxr;

                     if(sum > max)
                        max = sum;

                    // cout<<selected[0]<<" "<<selected[1]<<" "<<selected[2]<<"\n";
                     selected.clear();

                     // copy(selected.begin(), selected.end(), ostream_iterator<int>(cout, " "));
                 }
                 while (prev_permutation(selector.begin(), selector.end()));
                 cout<<setprecision(10);
                 cout<<fixed;

        cout<<"Case #"<<count<<": "<<max<<"\n";
        count++;

    }

  return 0;
}


