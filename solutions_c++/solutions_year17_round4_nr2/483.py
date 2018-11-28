#include <bits/stdc++.h>

using namespace std;

#define INF 100000000
#define YJ 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long
#define LD long double

using namespace std;

using II = pair<int, int>;

#define MAX_N 1005
#define MAX_M 1005
#define MAX_C 1005

bool debugFlag = false;

int T;
int N, C, M;
int P[MAX_N], B[MAX_N];

int Cnt[MAX_N];
vector<II> vec;
vector<II> SeatList;

int Last[MAX_C];
int PCnt[MAX_C];

void init()
{
  memset(Cnt, 0, sizeof(Cnt));
  memset(PCnt, 0, sizeof(PCnt));
  vec.clear();
  SeatList.clear();
}

//promotionは何回やってもいいからmid回でさばけるか
bool check(int mid)
{
  set<int> Set[MAX_C];

  for (int i = 0; i < M; i++) {
    bool flag = false;
    for (int j = 0; j < mid && !flag; j++) {
      if(Set[j].insert(B[i]).second){
        flag = true;
      }
    }
    if(!flag){
      return false;
    }
  }

  int Sum = 0;
  for (int i = 0; i < MAX_C; i++) {
    Sum += PCnt[i];
    if(Sum/mid + (Sum%mid > 0 ? 1 : 0) > i+1){
      return false;
    }
  }

  return true;
}

int main()
{
  cin >> T;
  for (int testCase = 1; testCase <= T; testCase++) {
    init();

    cin >> N >> C >> M;
    for (int i = 0; i < M; i++) {
      cin >> P[i] >> B[i];
      P[i]--; B[i]--;
      Cnt[B[i]]++;
      SeatList.push_back(II(P[i], B[i]));
      PCnt[P[i]]++;
    }

    for (int i = 0; i < C; i++) {
      vec.push_back(make_pair(Cnt[i], i));
    }

    sort(begin(vec), end(vec), greater<II>());

    int l = 0, r = MAX_C;
    while(r-l > 1){
      int mid = (r+l)/2;
      if(check(mid)){
        r = mid;
      }
      else{
        l = mid;
      }
    }

    int ans = 0;
    int width = 0;

    for (int i = N-1; 0 <= i; i--) {
      width = 0;
      while(PCnt[i] > 0){
        width++;
        if(width > r){
          ans += PCnt[i];
          break;
        }
        PCnt[i]--;
      }
    }

    printf("Case #%d: %d %d\n", testCase, r, ans);
  }

  return 0;
}
