#include <bits/stdc++.h>

using namespace std;

#define READ() 	    freopen("in.txt","r",stdin)
#define WRITE()     freopen("out.txt","w",stdout)
#define sf(n) 	    scanf("%d",&n)
#define sl(x)       scanf("%I64d",&x)
#define lsf(n) 	    scanf("%lld", &n)
#define pb(n) 	    push_back(n)
#define mem(x,y)    memset(x,y,sizeof(x))
#define D(x)      	cout << #x << " = " << x << endl
#define YOLO        cout << "YOLO" << endl
#define NL			printf("\n")
#define EPS 	    1e-10
#define INF         INT_MAX
#define MAX         INT_MAX
#define MOD         1000000007
#define LL          long long
#define endl        "\n"
#define pi          2.0*acos(0.0)
#define cnd         tree[idx]
#define lnd         tree[left]
#define rnd         tree[right]
#define callLeft    left,st,mid
#define callRight   right,mid+1,ed

bool chk(string s)
{
    for(int i=0;i<s.size() - 1;i++)
    {
        if(s[i] > s[i+1])return false;
    }
    return true;
}


string intToStr(LL x)
{
    string s = "";
    while(x > 0)
    {
        char c = x%10; x/=10;
        c += 48;
        s += c;
    }
    reverse(s.begin(),s.end());
    return s;
}

LL strToInt(string s)
{
    LL ret = 0;
    for(int i=0;i<s.size();i++)
    {
        LL x = s[i] - 48;
        ret *= 10;
        ret += x;
    }
    return ret;
}

LL burteSol(LL x)
{
    for(LL i=x;i>=0;i--)
    {
        if(chk(intToStr(i)))return i;
    }
}

int main()
{
//	ios_base::sync_with_stdio(false);
//    cin.tie(0); /// use "\n" instead of endl
#ifndef ONLINE_JUDGE
    READ();
    WRITE();
#endif
    int t;
    cin >> t;
    int TC = 0;
    while(t--)
    {
        LL x;
        cin >> x;
////        cout << strToInt(intToStr(x)) << endl;
//
//        printf("%4lld", strToInt(intToStr(x)));

//        cout << burteSol(x) << endl;
        string s = intToStr(x);
        int i = 0;
        bool genjam = false;
        string sAns = "";
        for(;i<s.size()-1;i++)
        {
            if(s[i] > s[i+1])
            {
                while(i > 0 && s[i] == s[i-1])
                {
                    i--;
                }
                s[i]--;
//                sAns += s[i];
//                int j = i-1;
//                if(j >= 0 && )
                genjam = true;
                break;
            }
            else
            {
//                sAns += s[i];
            }
        }
//        if(!genjam)sAns += s[i];
        for(int j=0;j<=i;j++)sAns += s[j];
        i++;
        for(;i<s.size();i++)
        {
            sAns += '9';
        }

//        i = 0;
//        while(sAns[i] == '0')i++;

        cout << "Case #" << ++TC << ": ";
//        for(;i<sAns.size();i++)cout << sAns[i];
//        cout << endl;

        LL ans = strToInt(sAns);

        cout << ans << endl;
//        if(ans != burteSol(x))
//        {
//            cout << x << endl;
//            YOLO;
//        }
    }




    return 0;
}

