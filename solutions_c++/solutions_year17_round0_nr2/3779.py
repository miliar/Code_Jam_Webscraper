#include <iostream>
#include <vector>

using namespace std;

template<typename T>
// integer T
vector<T> convert(T i) {
  vector<T> v;
  v.reserve(20);
  while (0 < i) {
    v.insert(begin(v), i % 10);
    i /= 10;
  }
  return v;
}

template<typename T, typename R>
int first(vector<T> const& v, R r) {
  for (int i = 0; i < v.size() -1; ++ i)
    if(r(v[i],v[i+1])) return i;
  return -1;
}

template<typename T>
int find_pos(vector<T> const& v) {
  int less = first(v, std::greater<T>());
  if (less == -1) return -1; // nothing to do
  int same = first(v, std::equal_to<T>());
  return same == -1 ? less :
    (v[same] < v[less] ? less : same);
}

template<typename T>
void set(vector<T> & v, int pos) {
  v[pos] = v[pos] - 1;
  for (++pos; pos < v.size(); ++pos) v[pos] = 9;
}

template<typename I>
void print(I f, I l) {
  while(f != l && *f == 0) ++f;
  while(f != l) { cout << *f; ++f; }
  cout << endl;
}

template<typename T>
void solve(T input) {
  auto v = convert<T>(input);
  int pos =  find_pos<T>(v);
  if (pos != -1)
    set(v, pos);
  print(begin(v), end(v));
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int i;
    cin >> i;
    cout << "Case #" << t+1 << ": ";
    if (i < 10)
      cout << i << endl;
    else
      solve(i);
  }
}
