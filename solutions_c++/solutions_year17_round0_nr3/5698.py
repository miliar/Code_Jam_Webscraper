#include <bits/stdc++.h>
using namespace std;
/*
void stall(int a[], int l, int r, int *k, int *ls, int *lr)
{
    (*k)--;
    int m = (l+r)/2;
    if((*k)==0)
    {
        *ls = m-l-1;
        *lr = r-m-1;
        return;
    }
    a[m] = 1;
    if((m-l)<(r-m))
        stall(a, l, m, k, ls, lr, );
    else stall(a, m, r, k, ls, lr);
}
*/
int main() {
    int t, n, ll, rr, k, i, j, l, r, ls, rs, min, max, c, m;
    cin>>t;
    for(c=1; c<=t; c++)
    {
        cin>>n>>k;
        int a[n+2] = {0};
        a[0] = a[n+1] = 1;
        ll = rr = 0;
        while(k)
        {
            ll = 1;
            rr = 0;
            for(i=1; i<n+1; i++)
            {
                if(a[i] == 0)
                {
                    for(j=i-1; j>=0; j--)
                        if(a[j]==1)
                        {
                           l = j;
                           break;
                        }

                    for(j=i+1; j<n+2; j++)
                    {
                        //cout<<"a[i] i="<<i<<" j="<<j<<"  a[j]="<<a[j]<<"\n";
                        if(a[j]==1)
                        {
                            r = j;
                            break;
                        }
                    }

                    //cout<<"i="<<i<<" l="<<l<<"  r="<<r<<"\n";

                    if((r-l)>(rr-ll))
                    {
                        ll = l;
                        rr = r;
                    } 
                }
            }
            //cout<<"ll="<<ll<<"  rr="<<rr<<"\n";
            m = (ll+rr)/2;
            a[m] = 1;
            k--;
            //for(i=0; i<n+2; i++) cout<<a[i]<<" "; cout<<"\n";
        }
        //cout<<"ll="<<ll<<"  rr="<<rr<<"\n";
        ls = m - ll-1;
        rs = rr - m-1;
        min = ls<rs? ls : rs;
        max = ls>rs? ls : rs;
        cout<<"Case #"<<c<<": "<<max<<" "<<min<<"\n";
    }
    return 0;
}