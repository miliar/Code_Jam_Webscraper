#include <cstdlib>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#define pp pair<double, double>
#define pi 3.1415926535
#define iter vector<pair<double, double>>::iterator
#define vc vector<pair<double, double>>
using namespace std;
int t;
int n, k;
vector<pp> data;
double expose;

void init(){
  expose = 0;
  data.clear();
  expose = 0;
}

void check(vc &a){
  for(iter it = a.begin(); it != a.end(); it++){
    printf("%f %f\n", it->first, it->second);
  }
}

void parse(){
  scanf("%d %d", &n, &k);
  for(int i = 0; i < n ; i++){
    pp tmp;
    scanf("%lf %lf", &tmp.first, &tmp.second);
    data.push_back(tmp);
  }
  //check(data);
}

double radius(pp a){
  return 2 * pi * a.first * a.second;
}

double area(pp a){
  return  pi * pow(a.first, 2);
}

bool mycmp(pp lhs, pp rhs){
  double a = 2 * pi * lhs.first * lhs.second;
  double b = 2 * pi * rhs.first * rhs.second;
  return a > b;
}

bool mycmp2(pp lhs, pp rhs){
  if(lhs.first == rhs.first){
    return lhs.second > rhs.second;
  }
  else{
    return lhs.first > rhs.first;
  }
}

void solve(){
  sort(data.begin(), data.end(), mycmp2);
  //printf("data sort\n"); check(data);
  for(int i = 0 ; i < n-k+1; i++){
    double sum = radius(data[i]) + area(data[i]);
    //printf("i:%d, sum %f\n", i, sum);
    vector<pp> data2 (data.begin() + i + 1, data.end());
    //printf("data cut \n");  check(data2);
    sort(data2.begin(), data2.end(), mycmp);
    for(int j = 0; j < k - 1; j++){
      sum += radius(data2[j]);
    }
    //printf("\ni %d sum: %f\n", i, sum);
    expose = max(expose, sum);
  }
  printf("%lf\n", expose);
}

int main(){
  scanf("%d" , &t);
  for(int i = 0; i < t; i++){
    printf("Case #%d: ", i + 1);
    init();
    parse();
    solve();
  }
}
