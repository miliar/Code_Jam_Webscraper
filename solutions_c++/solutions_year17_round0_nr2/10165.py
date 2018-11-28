#include <bits/stdc++.h>
using namespace std;

int n;


int check(string s)
{
    bool ok = true; int id;
    for(int i = n-1; i>=1; i--)
    {
        if(s[i] < s[i-1] || s[i]=='0')
        {
            ok = false;
            id = i;
            break;
        }
    }
    if(!ok) return id;
    return -1;
}


int main ()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen ("a2.out","w",stdout);
    int t,cs = 0; cin>>t;
    while(t--)
    {
        string S; cin>>S;
        cout<<"Case #"<<++cs<<": ";
        n = S.size();
       // if(n==1) cout<<S<<endl;

       int idx = 30;
        while(1)
        {
            int i = check(S);
            if(i==-1) break;
            else if(i < idx)
            {
                idx = i;
            }
            else if(i>idx) break;
            else
            {
                //cout<<i<<endl;
                if(S[i]=='0')
                {
                    while(i>=0 && S[i] =='0')
                    {
                        S[i]='9';
                        //cout<<S[i]<<endl;
                        i--;
                    }
                    //S[i] = '9';
                    char ch = S[i];
                    int X = ch - '0';
                    int rep = X - 1;
                    S[i] = rep + '0';
                }
                else
                {
                    S[i] = '9';
                    if(S[i-1]=='0')
                    {
                        int l = i-1;
                        while(l>=0 && S[l] =='0')
                        {
                            S[l]='9';
                          //  cout<<S[l]<<endl;
                            l--;
                        }
                    //S[i] = '9';
                        char ch = S[l];
                        int X = ch - '0';
                        int rep = X - 1;
                        S[l] = rep + '0';
                    }
                    else
                    {
                        char ch = S[i-1];
                        int X = ch - '0';
                        int rep = X - 1;
                        S[i-1] = rep + '0';
                    }
                }
                //cout<<S[i-1]<<endl;
            }
        }
        int init;
        for(int i = 0; i<n; i++)
        {
            if(S[i]=='0') continue;
            else
            {
                init = i;
                break;
            }
        }
        bool has = false;
        for(int i = init; i<n; i++)
        {
            if(S[i]!='9') cout<<S[i];
            else
            {
                has = true; init = i; break;
            }
        }
        while(has && init<n)
        {
            cout<<9; init++;
        }
        cout<<endl;
    }
    return 0;
}
