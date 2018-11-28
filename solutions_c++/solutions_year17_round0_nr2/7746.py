#include <assert.h>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

template<typename T>
ostream& operator<<(ostream& s, const vector<T>& c);

template<typename T>
ostream& operator<<(ostream& s, const set<T>& c);

template<typename T, typename TT>
ostream& operator<<(ostream& s, const map<T, TT>& c);

template<typename T>
ostream& operator<<(ostream& s, const vector<T>& c) {
  cout << '[';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it);
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << ']';
  return s;
}

template<typename T>
ostream& operator<<(ostream& s, const set<T>& c) {
  cout << '{';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it);
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << '}';
  return s;
}

template<typename T, typename TT>
ostream& operator<<(ostream& s, const map<T, TT>& c) {
  cout << '{';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it).first << ": " << (*it).second;
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << '}';
  return s;
}

template<typename T>
class vector2d {
 public:
  vector2d() {
  }

  vector2d(size_t n, size_t m) : n_(n), m_(m), v_(n * m) {
  }

  size_t size1() const {
    return n_;
  }

  size_t size2() const {
    return m_;
  }

  const T& operator()(size_t i, size_t j) const {
    assert(i < size1());
    assert(j < size2());
    return v_[i * size2() + j];
  }

  T& operator()(size_t i, size_t j) {
    assert(i < size1());
    assert(j < size2());
    return v_[i * size2() + j];
  }

 private:
  size_t n_{0};
  size_t m_{0};
  vector<T> v_;
};

template<typename T>
vector<int> ToDigits(T t, int r = 10) {
  vector<int> result;

  while (t) {
    result.push_back(t % r);
    t /= r;
  }

  reverse(result.begin(), result.end());

  return result;
}

template<typename T>
T FromDigits(const vector<int>& digits, int r = 10) {
  T result = 0;

  for (size_t i = 0; i < digits.size(); ++i) {
    result *= r;
    result += digits[i];
  }

  return result;
}

template<typename T>
T FindFactor(T t) {
  for (T i = 2; i * i <= t; ++i) {
    if (t % i == 0)
      return i;
  }

  return t;
}

template<typename T>
ostream& operator<<(ostream& s, const vector2d<T>& c) {
  size_t max_number_size = 2;
  for (size_t i = 0; i < c.size1(); ++i) {
    auto r = ToDigits(i, 10);
    max_number_size = max(max_number_size, r.size() + 1);

    for (size_t j = 0; j < c.size2(); ++j) {
      r = ToDigits(j, 10);
      max_number_size = max(max_number_size, r.size() + 1);

      r = ToDigits(c(i, j), 10);
      max_number_size = max(max_number_size, r.size() + 1);
    }
  }

  for (size_t i = 0; i < c.size1(); ++i) {
    size_t ii = c.size1() - i - 1;

    s << setw(max_number_size) << ii;
    for (size_t j = 0; j < c.size2(); ++j)
      s << setw(max_number_size) << c(ii, j);
    s << endl;
  }

  s << setw(max_number_size) << "";
  for (size_t j = 0; j < c.size2(); ++j)
    s << setw(max_number_size) << j;

  return s;
}

template<typename T>
void print_result(ofstream& out, const T& result) {
  cout << result;
  out << result;
}

template<typename T1, typename T2>
void print_result(ofstream& out, const T1& t1, const T2& t2) {
  cout << t1 << t2;
  out << t1 << t2;
}

template<typename T1, typename T2, typename T3>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3) {
  cout << t1 << t2 << t3;
  out << t1 << t2 << t3;
}

template<typename T1, typename T2, typename T3, typename T4>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3, const T4& t4) {
  cout << t1 << t2 << t3 << t4;
  out << t1 << t2 << t3 << t4;
}

template<typename T1, typename T2, typename T3, typename T4, typename T5>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3, const T4& t4, const T5& t5) {
  cout << t1 << t2 << t3 << t4 << t5;
  out << t1 << t2 << t3 << t4 << t5;
}

template<typename T1, typename T2, typename T3, typename T4, typename T5, typename T6>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3, const T4& t4, const T5& t5, const T6& t6) {
  cout << t1 << t2 << t3 << t4 << t5 << t6;
  out << t1 << t2 << t3 << t4 << t5 << t6;
}

template<typename T1, typename T2, typename T3, typename T4, typename T5, typename T6, typename T7>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3, const T4& t4, const T5& t5, const T6& t6, const T7& t7) {
  cout << t1 << t2 << t3 << t4 << t5 << t6 << t7;
  out << t1 << t2 << t3 << t4 << t5 << t6 << t7;
}

template <typename T>
vector<size_t> sort_indexes(const vector<T>& v, bool asc) {
  vector<size_t> idx(v.size());
  for (size_t i = 0; i < idx.size(); ++i)
    idx[i] = i;
  sort(idx.begin(), idx.end(),
    [&v, &asc](size_t i1, size_t i2) {
      if (asc)
        return v[i1] < v[i2];
      else
        return v[i1] > v[i2];
    }
  );
  return idx;
}

template<typename ContainerType>
bool asc(const ContainerType& v) {
  for (auto it = v.begin(); it != v.end(); ++it) {
    auto next = it;
    ++next;

    if (next == v.end())
      break;

    if ((*it) > (*next))
      return false;
  }

  return true;
}

int64_t solve(int64_t t) {
  for (int64_t i = t; i > 0; --i) {
    auto d = ToDigits(i);
    if (asc(d)) {
      return i;
    }
  }

  return 1;
}

int64_t solve2(int64_t t) {
  auto d = ToDigits(t);

  while (true) {
    bool ok = true;
    for (size_t i = 0; i + 1 < d.size(); ++i) {
      if (d[i] > d[i + 1]) {
        ok = false;

        for (size_t j = i + 1; j < d.size(); ++j)
          d[j] = 9;
        --d[i];
      }
    }

    if (ok)
      return FromDigits<int64_t>(d);
  }

  return 1;
}

int main(int argc, char* argv[]) {
  ifstream in_file("B-large.in");
  ofstream out_file("out.txt");

  int test_cases = 0;
  in_file >> test_cases;

  for (int case_index = 0; case_index < test_cases; ++case_index) {
    print_result(out_file, "Case #", case_index + 1, ": ");

    int64_t N = 0;
    in_file >> N;

    print_result(out_file, solve2(N));

    print_result(out_file, "\n");
  }
}