#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;
vector<vector<long long int>> p,a,a1,p1;
vector<vector<double>> d;


int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        int n,q;
        cin>>n>>q;
        vector<int> e,s;
        d.clear();
        p.clear();
        a.clear();


        for (int i=0;i<n;i++){
            int ee,ss;
            cin>>ee>>ss;
            e.push_back(ee);
            s.push_back(ss);
        }

        for (int i=0;i<n;i++){
            vector<long long int> tmp;
            vector<long long int> tmp1;
            vector<double> tmp2;
            for (int j=0;j<n;j++){
                int t;
                cin>>t;
                tmp.push_back(t);
                tmp1.push_back(j);
                tmp2.push_back(-1);
            }
            a.push_back(tmp);
            d.push_back(tmp2);
            p.push_back(tmp1);
        }
        a1=a;
        p1=p;
        for (int k=0; k<n; ++k)
            for (int i=0; i<n; ++i)
                for (int j=0; j<n; ++j)
                {
                    if ((a[i][j]==-1||(a[i][k] +a[k][j]<a[i][j]))&&a[i][k]!=-1&&a[k][j]!=-1){
                       a[i][j]=a[i][k] +a[k][j];
                       p[i][j]=k;
                    }
                }
       /* for (int i=0; i<n; ++i){
                    for (int j=0; j<n; ++j)
                        cout<<a[i][j]<<" ";
                    cout<<endl;
                }*/

        for (int k=0; k<n; ++k)
            for (int i=0; i<n; ++i)
                for (int j=0; j<n; ++j)
                {
                    if (e[i]>=a[i][j]&&a[i][j]!=-1)
                      if (d[i][j]==-1||d[i][j]>(a[i][j]+0.0)/s[i])
                        d[i][j]=(a[i][j]+0.0)/s[i];


                    if (a[i][k]!=-1&&a[k][j]!=-1){
                        if (e[i]>=a[i][k]+a[k][j])
                          if (d[i][j]==-1||d[i][j]>(a[i][k]+a[k][j]+0.0)/s[i])
                            d[i][j]=(a[i][k]+a[k][j]+0.0)/s[i];
                        if (e[i]>=a[i][k]&& e[k]>a[k][j])
                          if (d[i][j]==-1||d[i][j]>(a[i][k]+0.0)/s[i]+(a[k][j]+0.0)/s[k])
                            d[i][j]=(a[i][k]+0.0)/s[i]+(a[k][j]+0.0)/s[k];
                        if (d[i][k]!=-1&&d[k][j]!=-1)
                            if (d[i][j]==-1||d[i][j]>d[i][k]+d[k][j])
                                d[i][j]=d[i][k]+d[k][j];
                    }
                }

        /*for (int i=0; i<n; ++i){
            for (int j=0; j<n; ++j)
                cout<<d[i][j]<<" ";
            cout<<endl;
        }*/


            cout<<"Case #"<<(test+1)<<": "<<std::setprecision(9);
            for (int i=0;i<q-1;i++){
                int st,fs;
                cin>>st>>fs;
                cout<<d[st-1][fs-1]<<" ";
            }
            int st,fs;
            cin>>st>>fs;
            cout<<d[st-1][fs-1]<<endl;


    }




}
