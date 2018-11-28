#include<bits/stdc++.h>
using namespace std;
void fileMode()
{
    freopen("input2.in","r",stdin);
    freopen("output_file_name6.out","w",stdout);
}

int main()
{
    fileMode();
    int t;
    cin>>t;
    long long k,n,sR,lR,nSR,nLR,us,nU,d,l,s;
    for (int i = 0 ; i < t ; ++i)
    {
        cin>>n>>k;
        lR=sR=n;
        nLR = 1;
        nSR=us=0;
        d=nU= 1L;
        while (nU < k || nU < 0L)
        {
            us= nU;
            d*= 2L;
            nU=us+d;
            long long nnnLR = 0;
            long long nnnSR = 0;
            long long newLL,newSL,newSS,newLS;
            long long nnLR = lR - (1L + lR) / 2L;
            long long nnSR = (1L + sR) / 2L - 1L;
            nnSR = (nnSR < 0) ? 0 : nnSR;
            if (nLR > 0)
            {
                newLL = lR - (1L + lR) / 2L;
                newLS = (1L + lR) / 2L - 1L;
                newLS = (newLS < 0) ? 0 : newLS;
                nnnLR += (newLL == nnLR) ? nLR : 0;
                if (newLS == nnLR)nnnLR += nLR;
                else nnnSR += nLR;
            }
            if (nSR > 0)
            {
                newSL = sR - (1L + sR) / 2L;
                newSS = (1L + sR) / 2L - 1L;
                newSS = (newSS < 0) ? 0 : newSS;
                if (newSL == nnLR)nnnLR += nSR;
                else nnnSR += nSR;
                if (newSS == nnLR)nnnLR += nSR;
                else nnnSR += nSR;
            }
            lR = nnLR;
            sR = nnSR;
            nLR = nnnLR;
            nSR = nnnSR;
        }
        if (k - us <= nLR)
        {
            l = lR - (1L + lR) / 2L;
            s = (1L + lR) / 2L - 1L;
            s = (s < 0) ? 0 : s;
            cout<<"Case #"<<i+1<<": "<<l<<" "<<s<<"\n";
        }
        else
        {
            l = sR - (1L + sR) / 2L;
            s = (1L + sR) / 2L - 1L;
            s = (s < 0) ? 0 : s;
            cout<<"Case #"<<i+1<<": "<<l<<" "<<s<<"\n";
        }
    }
}
