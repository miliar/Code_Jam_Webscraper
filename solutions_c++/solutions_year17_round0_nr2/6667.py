#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
int strSize;
ll maxForLength[20];
ll dp[11][20];

/// I am sick and do not have energy to debug why on earth
/// this version of gnu do not support to_string().. So meh!
namespace custom
{
template<typename T> string to_string(const T& val)
{
    ostringstream stream;
    stream << val;
    return stream.str();
}
}

ll BigMod(ll val,ll power)
{
    if(power <= 0) return 1;
    if(power&1)
    {
        return val * BigMod(val,power-1);
    }
    else
    {
        ll half = BigMod(val,power>>1);
        return half*half;
    }
}

ll rec(int lastDigit,int len)
{
    if(len <= 0) return 0LL;
    ll &ret = dp[lastDigit][len];
    if(ret > -1) return ret;

    for(int i=lastDigit; i<10; i++)
    {
        ll number = BigMod(10LL,len-1)*(ll)i;
        ret = max(ret, rec(i,len-1)+number);
    }
    return ret;
}

ll GetMaxForLength(ll len)
{
    if(len == 0) return 0;
    if(maxForLength[len] > 0) return maxForLength[len];

    ll cur = BigMod(10LL,len-1) * 9LL;
    ll prev = GetMaxForLength(len-1);

    maxForLength[len] = cur+prev;
    return maxForLength[len];
}

ll calc(ll limit)
{
    ll ret = 0LL;
    string limStr = custom::to_string(limit);
    strSize = limStr.size();
    ret = max(ret,GetMaxForLength(strSize-1));

    ll firstDigit = (ll)limStr[0]-'0';
    ll beforeIthIndex = (BigMod(10LL,strSize-1)*firstDigit);

    for(int i=1; i<firstDigit; i++)
    {
        ret = max( ret, rec(i,strSize-1)+ BigMod(10LL,strSize-1)*(ll)i );
    }
    ll minDigit = firstDigit;
    for(int i=1; i<strSize; i++)
    {
        ll curDigit = (ll) limStr[i]-'0';
        for(int j=minDigit; j<curDigit; j++)
        {
            ll tillIthIndex = beforeIthIndex + BigMod(10LL,strSize-i-1)*(ll)j;
            ll afterIthIndex = rec(j,strSize-i-1);
            ll curVal = tillIthIndex + afterIthIndex;
            if(curVal > limit) curVal = -100;
            ret = max( ret, curVal);
        }
        if(curDigit > minDigit) minDigit = curDigit;
        beforeIthIndex += (BigMod(10LL,strSize-i-1)*minDigit);
    }
    if(beforeIthIndex <= limit){
        ret = max(ret, beforeIthIndex);
    }
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("a.in","r+",stdin);
    freopen("a.out","w+",stdout);
    int T,cas=0;
    cin>>T;
    memset(dp,-1LL,sizeof dp);
    memset(maxForLength,-1LL,sizeof maxForLength);
    while(T--)
    {
        ll limit;
        cin>>limit;
        ll ans = 1LL;
        ans = max(ans, calc(limit));
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    return 0;
}
/// 12321 => 12299
/// 4321 => 3999
