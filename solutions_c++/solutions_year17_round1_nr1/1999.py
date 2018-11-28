#include<bits/stdc++.h>
//#include "A-small-practice.in"
#include <fstream>
#define pb push_back
#define mp make_pair
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1L.out","w",stdout);
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        int R, C;
        cin>>R>>C;
        vector<string> mat;
        string s;
        vector< pair<int,int> > v;
        for(int i=0;i<R;i++)
        {
            cin>>s;
            mat.pb(s);
            for(int j=0;j<s.size();j++)
                if(mat[i][j]!='?')
                    v.pb(mp(i,j));

        }
        for(int i=0;i<v.size();i++)
        {
            int fir=v[i].first, sec=v[i].second;
            if(fir-1 >= 0)
            {
                for(int j=fir-1;j>=0;j--)
                {
                    if(mat[j][sec]!='?')
                        break;
                    else
                        mat[j][sec]=mat[fir][sec];
                }
            }
            if(fir+1<R)
            {
                for(int j=fir+1;j<R;j++)
                {
                    if(mat[j][sec]!='?')
                        break;
                    else
                        mat[j][sec]=mat[fir][sec];
                }
            }

        }

        for(int i=0;i<v.size();i++)
        {
           int fir=v[i].first, sec=v[i].second;
            for(int k=fir;k<R;k++)
            {
                for(int j=sec-1;j>=0;j--)
                {
                    if(mat[k][j]!='?')
                        break;
                    else
                        mat[k][j]=mat[k][sec];
                }

                for(int j=sec+1;j<C;j++)
                {
                    if(mat[k][j]!='?')
                        break;
                    else
                        mat[k][j]=mat[k][sec];
                }
            }
            for(int k=fir;k>=0;k--)
            {
                for(int j=sec-1;j>=0;j--)
                {
                    if(mat[k][j]!='?')
                        break;
                    else
                        mat[k][j]=mat[k][sec];
                }

                for(int j=sec+1;j<C;j++)
                {
                    if(mat[k][j]!='?')
                        break;
                    else
                        mat[k][j]=mat[k][sec];
                }
            }
        }
        /*for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(mat[i][j]=='?')
                {
                    for(int k=j;k<C;k++)
                    {
                        if(mat[i][k]!='?')
                        {
                            for(int i1=i;i1<R;i1++)
                                for(j1=j;j2<k;j2++)
                                    mat[i1][j1]=mat[i1][k];
                            break;
                        }
                    }
                    for(int k=j;k>=0;k--)
                    {
                        if(mat[i][k]!='?')
                        {
                            for(int i1=i;i1<R;i1++)
                                for(j1=j;j2<k;j2++)
                                    mat[i1][j1]=mat[i1][k];
                            break;
                        }
                    }*/

                    /*if(j-1>=0)
                        if(mat[i][j-1]!='?')
                            mat[i][j]=mat[i][j-1];
                    else if(j+1<R)
                        if(mat[i][j+1]!='?')
                            mat[i][j]=mat[i][j+1];*/
            cout << "Case #" << t+1 << ":\n";
            for(int i=0;i<R;i++)
            {
                for(int j=0;j<C;j++)
                    cout<<mat[i][j];
                cout << endl;
            }

        }

    return 0;
}
