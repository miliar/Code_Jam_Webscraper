#include <bits/stdc++.h>
using namespace std;

struct interval
{
    int L, R;
    int which;
};

bool operator <(const interval& A, const interval& B)
{
    return A.L<B.L;
}

int lA, lB;
const int MX=209;
interval A[MX], B[MX];

interval AB[MX];

const int MAXT=24*60;



int solve()
{
    for(int i=0; i<lA; i++)
    {
        AB[i]=A[i];
        AB[i].which=0;
    }
    for(int i=0; i<lB; i++)
    {
        AB[lA+i]=B[i];
        AB[lA+i].which=1;
    }

    vector<int> leftover={720, 720};


    int l=lA+lB;
    for(int i=0; i<l; i++)
    {
        leftover[AB[i].which]-=AB[i].R-AB[i].L;
    }

    vector<int> temp_left=leftover;


    sort(AB, AB+l);

    multiset<int> M[2];
    int ans=0;

    for(int i=0; i+1<l; i++)
    {
        if(AB[i].which==AB[i+1].which)
        {
            int w=AB[i].which;
            int len=AB[i+1].L-AB[i].R;
            M[w].insert(len);
        }
        else
        {
            ans++;
        }
    }

    if(AB[l-1].which==AB[0].which)
    {
        int w=AB[0].which;
        int len=(24*60-AB[l-1].R)+AB[0].L;
        M[w].insert(len);
    }
    else ans++;

    cerr << "ANS: " << ans <<endl;

    //M[AB[0].which].insert(AB[0].L);
    //M[AB[l-1].which].insert(24*60-AB[l-1].R);
    multiset<int> Mtemp[2];
    Mtemp[0]=M[0];
    Mtemp[1]=M[1];

    int result=10000;
    //for(int cover_first=0; cover_first<2; cover_first++)
    //for(int cover_last=0; cover_last<2; cover_last++)
    {
        M[0]=Mtemp[0];
        M[1]=Mtemp[1];
        leftover=temp_left;

        //int temp=(1-cover_first)+(1-cover_last);

        //if(cover_first) leftover[AB[0].which]-=AB[0].L;
        //if(cover_last) leftover[AB[l-1].which]-=(24*60-AB[l-1].R);

        //if(leftover[0]<0 || leftover[1]<0) continue;

        for(int which=0; which<2; which++)
        {
            while(!M[which].empty() && *(M[which].begin())<=leftover[which])
            {
                /*
                for(auto bla: M[which])
                {
                    cerr << which << ": " << bla << endl;
                }
                cerr << "------" << endl;
                */

                leftover[which]-=*(M[which].begin());
                M[which].erase(M[which].begin());
            }

            cerr << "DBG M:" << endl;

            for(auto bla: M[which])
                {
                    cerr << which << ": " << bla << endl;
                }
                cerr << "------" << endl;
        }

        //cerr << cover_first << ' ' << cover_last << ' ' << endl;
        //cerr << ans << ' ' << temp << ' ' << M[0].size() << ' ' << M[1].size() << endl;
        result=ans+2*((int)M[0].size()+(int)M[1].size());

        //result=min(result, ans + temp + 2*((int)M[0].size()+(int)M[1].size()));;
    }

    return result;
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> lA >> lB;
        for(int i=0; i<lA; i++)
        {
            cin >> A[i].L >> A[i].R;
        }
        for(int i=0; i<lB; i++)
        {
            cin >> B[i].L >> B[i].R;
        }
        int result=solve();

        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}
