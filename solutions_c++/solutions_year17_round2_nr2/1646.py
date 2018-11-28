#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b)                for(ll i=a;i<b;i++)
#define repr(i,n)                for(ll i=n-1;i>=0;i--)
#define ll long long int
#define ld long double
#define llu long long unsigned
#define pb push_back
#define mod 1e9+7

/*
                    ** author **
                ** Parth Lathiya **
    ** https://www.cse.iitb.ac.in/~parthiitb/ **
*/

int main()
{

ios::sync_with_stdio(false);

#ifndef ONLINE_JUDGE
	freopen("B-small-attempt1.in","r",stdin);
#endif

freopen("B-small-attempt1.out","w",stdout);

//  --------------------------------------------------------------------------------------

    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
        int N, R, O, Y, G, B, V;
        cin>>N>>R>>O>>Y>>G>>B>>V;
        // cout<<T;
        char ans[1001];
        char pr;
        // cout<< N;
        if(R>0){pr='R';R--;}
        else if(B>0){pr='B';B--;}
        else if(Y>0){pr='Y';Y--;}
        int flag=0,i=0;
        N--;
        // cout<<N<<R<<Y<<B;
        while(N--)
        {
            ans[i++]=pr;
            // cout<<N<<pr<<R<<Y<<B;
            if(pr=='R')
            {
                if(B>Y && B>0){pr='B';B--;}
                else if(Y>0){pr='Y';Y--;}
                else{flag=1;break;}
            }
            else if(pr=='B')
            {
                if(R>Y && R>0){pr='R';R--;}
                else if(Y>0){pr='Y';Y--;}
                else{flag=1;break;}

            }
            else if(pr=='Y')
            {
                if(B>R && B>0){pr='B';B--;}
                else if(R>0){pr='R';R--;}
                else{flag=1;break;}
            }
            // if(N!=1 && !R && !O && !Y){flag=1;break;}
        }
        if(flag==0){if(pr==ans[0])flag=1;}
        if(flag==1){cout<<"Case #"<<bk-T<<": "<<"IMPOSSIBLE"<<endl;}
            else
            {
                ans[i++]=pr;
                ans[i]='\0';
                cout<<"Case #"<<bk-T<<": "<<ans<<endl;
            }
    }

//  --------------------------------------------------------------------------------------

return 0;
}