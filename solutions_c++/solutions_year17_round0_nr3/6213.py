#include<bits/stdc++.h>

typedef long long int lli;
using namespace std;

//int mat[1000010][3];
vector<vector<int> > mat(1000001, vector<int>(3));
int cnt=0;

bool my_compare(vector<int> &lhs, vector<int> &rhs)
{
    return (lhs[2]> rhs[2]);
}

lli get_I(lli L, lli R)
{
    int mid = R-L+1;
    int I=L+mid/2;
    if(!(mid&1))
        I-=1;
    return I;
}

void find_place(int L, int R)
{
    int I=get_I(L,R);
    //cout<<L<<"  "<<R<<"  "<<I<<endl;
    mat[cnt][0]=I-L;
    mat[cnt][1]=R-I;
    mat[cnt][2]=(I-L) + (R-I);
    cnt++;
    if(L == R)
        return;
    if(I-1 >= L)
        find_place(L,I-1);

    if(I+1 <= R)
        find_place(I+1,R);
}

int main()
{
    int T;
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin>>T;
    for(int j=1;j<=T;j++)
    {
        lli N, K;
        cin>>N>>K;
        cnt=0;
        find_place(1,N);
        /*if(N <= 00)
        {
        cout<<"Matrix => "<<endl;
        for(int i=0;i<cnt;i++)
        {
            cout<<mat[i][0]<<"  "<<mat[i][1]<<"  "<<mat[i][2]<<endl;
        }
        }*/
        sort(mat.begin(),mat.begin() + cnt, my_compare);
       /* if(N <= 0)
        {
        cout<<"Matrix = "<<endl;
        for(int i=0;i<cnt;i++)
        {
            cout<<mat[i][0]<<"  "<<mat[i][1]<<"  "<<mat[i][2]<<endl;
        }
        }*/
        cout<<"Case #"<<j<<": ";
        cout<<max(mat[K-1][0],mat[K-1][1])<<" "<<min(mat[K-1][0],mat[K-1][1])<<endl;
    }
    return 0;
}

