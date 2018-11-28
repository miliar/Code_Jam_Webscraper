#include <bits/stdc++.h>
#define ll long long
#define ull unsigned ll

using namespace std;
#define MAXN 150001
#define files(x) freopen((x+string(".dat")).c_str(), "r", stdin); //freopen((x+string(".sol")).c_str(), "w", stdout);
#define int ll


#define MAXN 1000001
#define input_file(x) freopen((x+string(".txt")).c_str(), "r", stdin);
#define output_file(x) freopen((x+string(".txt")).c_str(), "w", stdout);




int gcd (int a, int b, int & x, int & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	int x1, y1;
	int d = gcd (b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}


int inv(int a, int m){
    int x, y;

    int g = gcd (a, m, x, y);
    if (g != 1)

        cout << "no solution";
    else {
        x = (x % m + m) % m;
        return x;
    }
}
/*int next(int from, int cur, int base){
    return ((cur+2) * inv(from, base))%base;
}*/

bool check(string s, int n){
    if (s[0] == s[s.size()-1])
        return false;
    if (s.size()!=n)
        return false;
    for (int i=0;i<s.size()-1;i++)
        if (s[i] == s[i+1])
        return false;

    return true;
}

string solve(){
            int n;
            cin>>n;
            int a[6];
//            cin>>a[0]>>a[1]>>a[]]
            cin>>a[0]>>a[1]>>a[2]>>a[3]>>a[4]>>a[5];
            string names[6] = {"R", "O", "Y", "G", "B", "V"};


            string ans = "";
            int cnt = n;
            int cur = 0;
            for (int i=0;i<6;i++)
                if (a[i]>a[cur])
                    cur = i;
            ans+=names[cur];
            int first = cur;
            while (cnt>1){
                int next = -1, next_val = -1;
                for (int i=0;i<6;i++)
                    if (abs(i - cur)>1 && a[i]>next_val && a[i]>0){
                        next_val = a[i];
                        next = i;
                    }

                if (next==-1)
                    return "IMPOSSIBLE";
                if (abs(cur - first) > 1 && a[first] == a[next])
                    next = first;
                a[cur]--;
                cur = next;
                cnt--;
                ans+=names[cur];


            }

            /*

            while(cnt>0){
            for (int i=0;i<6;i++)
                if (a[i]>0){
                    a[i]--;
                    ans+=names[i];
                    cnt--;
                }
            }*/
            if (!check(ans, n))
            //if (ans[0] == ans[ans.size()-1])
                return "IMPOSSIBLE";
            /*
            if (!check(ans, n))
                cerr<<" SHIT";*/
            return ans;
}


main () {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    input_file("input");
   output_file("output");
    int t;
    cin>>t;
    for (int test_id = 1;test_id<=t;test_id++){

            cout<<"Case #"<<test_id<<": "<<solve()<<endl;









    }



}
