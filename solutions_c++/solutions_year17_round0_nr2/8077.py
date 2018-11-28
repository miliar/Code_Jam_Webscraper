#include<bits/stdc++.h>

using namespace std;

#define sd(a) scanf("%d", &a)
#define sd2(a,b) scanf("%d %d", &a, &b)
#define sd3(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sd4(a,b,c,d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define sll(a) scanf("%lld", &a)
#define sll2(a,b) scanf("%lld %lld", &a, &b)
#define sll3(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define sll4(a,b,c,d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
#define sc(a) scanf("%c", &a)
#define slf(a) scanf("%lf", &a)
#define slf2(a,b) scanf("%lf %lf", &a, &b)
#define slf3(a,b,c) scanf("%lf %lf %lf", &a, &b, &c)
#define slf4(a,b,c,d) scanf("%lf %lf %lf %lf", &a, &b, &c, &d)

#define FORN(i,n) for(int i = 0; i < n; i++)
#define all(v) v.begin(), v.end()
#define in(a,b) ( (b).find(a) != (b).end())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

#define BUFF ios::sync_with_stdio(false);

#define MAXN 10100

#define cin in
#define cout out

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

bool check(string s){
    for(int i = 0; i < s.size() - 1; i++){
        if(s[i] > s[i+1]) return false;
    }
    return true;
}

int main(){
    ifstream in;
    ofstream out;
    in.open("input.in");
    out.open("out.txt");

    string num,aux;


    int t;
    cin >> t;
    int cs = 1;
    while(cs <= t){
        cin >> num;
        while(!check(num)){
            aux.clear();
            for(int i = 1; i < num.size(); i++){
                if(num[i] < num[i-1]){
                    num[i-1] = max(48, num[i-1]-1);
                    while(i < num.size()){
                        num[i] = '9';
                        i++;
                    }
                }

            }
            //cout << aux << "aa" << endl;
            //cout << num << "UU" << endl;
            while(num[0] == '0'){
                num.erase(num.begin());
            }
            //system("pause");
        }


        cout << "Case #" << cs++ << ": " << num << endl;
    }

    in.close();
    out.close();
    return 0;

}
