#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool func(int a, int b){
  return (a > b);
}

int main(){
  int t, x, y, s1, s2, c = 0;

  cin >> t;
  for(int i = 0; i < t; i++){
    vector<int> vec;
    cin >> x >> y;
    vec.push_back(x);
    for(int j = 0; j < y; j++){
      if(vec[0] % 2 == 0){
        s1 = (vec[0] - 1) / 2 + 1;
	s2 = (vec[0] - 1) / 2;
	vec.push_back(s1);
	vec.push_back(s2);
	vec.erase(vec.begin());
	sort(vec.begin(), vec.begin() + vec.size(), func);
      }else{
        s1 = (vec[0] - 1) / 2;
	s2 = (vec[0] - 1) / 2;
	vec.push_back(s1);
	vec.push_back(s2);
	vec.erase(vec.begin());
	sort(vec.begin(), vec.begin() + vec.size(), func);
      }
      if(s1 == 0)
        break;
    }
    c++;
    cout << "Case #" << c << ": " << s1 << " " << s2 << endl;
  }
  return 0;
}
