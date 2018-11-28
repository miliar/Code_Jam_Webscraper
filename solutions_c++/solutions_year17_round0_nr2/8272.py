#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<iterator>
#include<gmpxx.h>

struct solver_2017_q_a {
  bool is_tidy (mpz_class a) {
    std::string a_str = a.get_str();
    int last_d = 0, d;
    unsigned char c_zero = '0';
    for(int i = 0; i < a_str.size(); ++i) {
      d = a_str[i] - c_zero;
      if(d >= last_d) {
        last_d = d;
      }else{
        return false;
      }
    }
    return true;
  }

  mpz_class max_candidate_tidy (mpz_class a) {
    mpz_class retval;
    std::string n;
    std::string a_str = a.get_str();
    int last_d = 0, d;
    int index_decr = 0;
    unsigned char c_zero = '0', c_one = '1', c_nine = '9';
    // std::cerr << "size: " << a_str.size() << std::endl;
    for(int i = 0; i < a_str.size(); ++i) {
      d = a_str[i] - c_zero;
      if(d >= last_d) {
        last_d = d;
      }else{
        // first decreasing point
        index_decr = i;
        break;
      }
    }
    // std::cerr << index_decr << std::endl;
    if(index_decr == 0) {
      // std::cerr << "OK" << std::endl;
      return a;
    }else if(index_decr == 1) {
      // std::cerr << "type a" << std::endl;
      if(a_str[0] != c_one) {
        // std::cerr << "20xx" << std::endl;
        // 2 to 9
        n = (a_str[0] - 1);
      }
      for(int i = 1; i < a_str.size(); ++i) {
        n.push_back(c_nine);
      }
      // std::cerr << n << std::endl;
      retval = n;
      return retval;
    }else if(index_decr < a_str.size()){
      // std::cerr << "type b" << std::endl;
      for(int i = 0; i < index_decr - 1; ++i) {
        n.push_back(a_str[i]);
        // std::cerr << n << std::endl;
      }
      // subtract 1 before
      n.push_back(a_str[index_decr -1] - 1);
      // std::cerr << n << std::endl;
      for(int i = index_decr; i < a_str.size(); ++i) {
        n.push_back(c_nine);
        // std::cerr << n << std::endl;
      }
      retval = n;
      return retval;
    }
    return a;
  }
  std::string run(std::string S) {
    mpz_class n, a;
    n = S;
    if(is_tidy(n)) {
      return S;
    }
    a = n;
    do {
      a = max_candidate_tidy(a);
    }while (!is_tidy(a));
    return a.get_str();
  }

};

int main(void) {
  solver_2017_q_a solver;

  int T, K, N;
  std::string S;

  /*
  mpz_class n;
  n = "110";
  std::cout << solver.max_candidate_tidy(n);
  return 0;
  */
  
  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    std::cin >> S;
    // std::cerr << K << S << std::endl;
    std::cerr << "Case #" << (i + 1);
    std::cout << "Case #" << (i + 1) << ": " << solver.run(S) << std::endl;
  }

  return 0;
}
