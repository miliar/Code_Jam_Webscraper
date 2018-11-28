#include <bits/stdc++.h>
#define f(i,a,b,s) for (int i = a; i <= b; i = i + s)

using namespace std;

string int_to_str(int num)
{
    stringstream ss;
    ss << num;
    return ss.str();
}

int str_to_int(string str)
{
    stringstream ss(str);
    int num;
    ss >> num;
    return num;
}

string tidy(string N)
{
    if (N.length() ==  1) return N;
    int k = -1;
    f(i,0,N.length()-2,1)
    {
        if (N[i+1] < N[i])
        {
            k= i;
            break;
        }
    }
    if (k == -1) return N;
    int val = 0;
    //  cout << "k:" <<  k << "\n";
    /* f(u,k,1,-1)
     {
         if (N[u-1] != N[u])
             {val =  u; break;}
     }*/
    for (int u = k; u >= 1 ; u--)
    {
        if (N[u-1] != N[u])
        {
            val =  u;
            break;
        }
    }
    // cout << "val:" <<  val << "\n";
    if (val != 0 )
    {
        string s3;
        if (N.length()- val -1 >= 1)
        {
            string s2(N.length()- val -1,'9');
            s3 = s2;
        }
        return N.substr(0,val) +  int_to_str(str_to_int(N.substr(val,1)) - 1)  +  s3;
    }
    else
    {
        //cout << "N[va]:" << N[val] << "\n";
        string s(N.length()-1, '9');
        if (N[val] == '1')
            return s;
        else
            return int_to_str(str_to_int(N.substr(val,1)) - 1) + s;
    }
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
    int tc;
    cin >> tc;
    f(i,1,tc,1)
    {
        string N;
        cin >> N;
        cout << "Case #"  << i <<": " << tidy(N) << "\n";
    }
    return 0;
}
