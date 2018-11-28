
/*
ID: peterpa3
PROG: beads
LANG: C++11
*/


#include <bits/stdc++.h>
#include <iomanip>
#include <limits>


#include <iostream>
#include <fstream>
#include <string>
using namespace std;


typedef vector<string> vs;
typedef vector<int> vi;
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)

typedef long long ll;
typedef vector<ll> vll;


#define ALL(v) v.begin(), v.end()
#define CLEAR(s) memset(s, 0, sizeof s)
#define MOD 1000000007;
#define PRINTA(s) cout << "\n Array " << #s << " :\n"; for(int i = 0; i < s.size(); ++i) cout << s[i] << " "; cout << "\n";
#define PRINTA2(s, n) cout << "\n Array " << #s << " :\n"; for(int i = 0; i < n; ++i) cout << s[i] << " "; cout << "\n";


#define UNTIL(n) for (int i =0; i< n; ++i)

# define MY_PI           3.14159265358979323846

int main(int argc, char *argv[])
{
   std::ios::sync_with_stdio(false);
   int ca = 0; int T;
   cin >> T;
   vector<pair<double, double>> stak;
//   int next = 0;
   while (ca < T)
   {
       ca++;
       cout << "Case #" << ca << ": ";
       // code goes here
       stak.clear();
       int N,K;
       cin >> N >> K;
       UNTIL(N)
       {
           int R,H;
           cin >> R >> H;
           pair<int, int> p = {R, H};
           stak.push_back(p);
       }

       sort(ALL(stak),[](const pair<int, int> & p1, const pair<int, int> &p2) -> bool
       {
           if (p1.first != p2.first) return p1.first > p2.first;
           else return p1.second > p2.second;
       });
       double ans = 0;
       vector<double> area;
       FOR(i,0,stak.size()- K)
       {
           double cur = 0.0;
           cur+= 2*MY_PI* double(stak[i].first) * double(stak[i].second);
           cur+= MY_PI* double(stak[i].first) * double(stak[i].first);
//           cout << cur << "\n";
           area.clear();
           FOR(j,i + 1,stak.size()-1)
           {
              area.push_back(2*MY_PI* double(stak[j].first) * double(stak[j].second));
           }

           sort(ALL(area),std::greater<double>());
//           cout << area.size() << "\n";
           FOR(j,0,K-2)
              cur+= area[j];
//           cout << cur << "\n";
           ans = max(ans, cur);
       }
       //cout.precision(18);
       cout << std::fixed << std::setprecision(22) << ans;
       //PRINTA(stak);
//       cout << "\n Array stak" << " :\n";
//       for(int i = 0; i < stak.size(); ++i)
//           cout  << "[" << stak[i].first << "|" << stak[i].second << "] ";
//       cout << "\n";


       // end code here
       cout <<   "\n";
   }
   return 0;
}

//int main() {
//    ofstream fout ("beads.out");
//    ifstream fin ("beads.in");
//    int n; fin >> n;
//    string s; fin >> s;

//    int ans = 0;
//    FOR(i,0,s.size()- 1)
//    {
//        //cut here
//        int cur = i;
//        int cur_ans = 0;
//        char c = 'd';
//        int count = 0;
//        while(count < n && (s[cur]=='w' || c == 'd' || (c!='d' && s[cur] == c)))
//        {
//            if(c=='d' && s[cur]!= 'w') c = s[cur];
//            ++cur_ans;
//            ++count;
//            cur = cur + 1 >= n? 0 : cur + 1;
//        }
//        cur = i - 1>= 0? i-1 : n-1;
//        c = 'd';
//        count = 0;
//        while(count < n && (s[cur]=='w' || c=='d' ||  (c!='d' && s[cur] == c)))
//        {
//            if(c=='d' && s[cur]!= 'w') c = s[cur];
//            ++cur_ans;
//            ++count;
//            cur = cur - 1 >= 0? cur -1 : n-1;
//        }
////        cout << cur_ans << " ";
//        ans = max(ans, min(n, cur_ans)); //,
//    }
////    cout << "\n";
//    fout << ans << "\n";
//    return 0;
//}






//using namespace std;




//int sum1ton(int n)
//{
//    return (n*(n+1))/2;
//}

//int max_n_sum_smaller_than(int k)
//{
//    return int((sqrt(double(1+ 8 * k)) -1)/2.0);
//}

////int max_n_sum_smaller_than_v2(int k)
////{
////    int high = floor(sqrt(2*k));
////    int low = ceil(sqrt(2*k)) - 1;
////    int ans = low;
////    for (int k = low; k <= high; ++k)
////    {
////        if ((sum1ton(k) <= k) && (ans < k))
////            ans = k;
////    }
////    return ans;
////}




////======================================================================================
