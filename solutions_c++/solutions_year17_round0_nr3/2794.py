#include <iostream>
#include <fstream>

int main() {
  std::ifstream in;
  in.open("test.in");
  std::ofstream out;
  out.open("test.out");
  
  int nb_tests;
  in >> nb_tests;

  for (int id_test = 1; id_test <= nb_tests; ++id_test) {
    long long N, K;
    in >> N >> K;

    if (K == 1) {
      out << "Case #" << id_test << ": " 
          << (N >> 1) << " "
          << ((N & 1) ? (N >> 1) : ((N >> 1) - 1)) << "\n";
      continue;
    }

    long long l1 = -1, n1 = 0, l2 = -1, n2 = 0;

    if (N & 1) {
      l1 = (N >> 1);
      n1 = 2;
      l2 = -1;
      n2 = 0;
    } else {
      l1 = (N >> 1) - 1;
      n1 = 1;
      l2 = (N >> 1);
      n2 = 1;
    }

    //std::cerr << l1 << " " << n1 << ";" << l2 << " " << n2 << "\n";
    
    long long clients = 1;
    while (clients + n1 + n2 < K) {
      clients += n1 + n2;

      long long new_l1 = -1, new_n1 = 0, new_l2 = -1, new_n2 = 0;
      if (l1 & 1) {
        new_l1 = (l1 >> 1);
        new_n1 = 2 * n1;
      } else {
        new_l1 = (l1 >> 1) - 1;
        new_n1 = n1;
        new_l2 = (l1 >> 1);
        new_n2 = n1;
      }

      if (l2 != -1) {
        if (l2 & 1) {
          new_n2 += 2 * n2;
        } else {
          new_n1 += n2;
          new_l2 = (l2 >> 1);
          new_n2 += n2;
        }
      }
      
      l1 = new_l1;
      n1 = new_n1;
      l2 = new_l2;
      n2 = new_n2;

      //std::cerr << l1 << " " << n1 << ";" << l2 << " " << n2 << "\n";
    }

    if (clients + n2 >= K) {
      out << "Case #" << id_test << ": " 
          << (l2 >> 1) << " " 
          << ((l2 & 1) ? (l2 >> 1) : ((l2 >> 1) - 1)) << "\n";
      continue;
    }

    out << "Case #" << id_test << ": " 
        << (l1 >> 1) << " "
        << ((l1 & 1) ? (l1 >> 1) : ((l1 >> 1) - 1)) << "\n";
  }

  return 0;
}
