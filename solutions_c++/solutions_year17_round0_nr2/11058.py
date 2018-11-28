
#include<iostream>
#include<fstream> 
using namespace std;



int dahai_jawab(long long x) {
  long long i = 1;
  while (x >= 10) {
    x = x / 10;
    i++;
  }
  return i;
}

bool tidy_number(long long number, long long dahai_value, int casenum) {
  long long check_digit = -1;
  long long i = dahai_value;
  long long zarb = 1;
  long long minus_number = number;
    int pCheckdigit =-1;
  long long x = 10;
  for (long long ii = dahai_value; ii > 1; ii--)
    zarb = zarb * x;

  //long long zarb = dahai_zarb(dahai_value);
  //cout<< endl << "zarb" << zarb << "number" << number <<"minus_number" << minus_number << "check_digit" << check_digit <<      endl;
  while (i > 0 && minus_number >= check_digit) {
    // cout<< "---- iteration ----" << i << endl;
    //cout<< "number" << minus_number << "  / zarb " << zarb << endl;
    if ((check_digit == 0 && minus_number > check_digit)||(pCheckdigit > check_digit))
      return false;
    
    pCheckdigit=check_digit;
    check_digit = minus_number / zarb;
    
    //cout<< "check_digit" << check_digit << endl;
    //cout<< "minus_number" << minus_number << endl;
    
    
    minus_number = (minus_number % zarb);
    zarb = zarb / 10;
    
    i--;
  }
  //cout<< "i =>" << i << endl;
  if (i > 0 || i < 0)
    return false;
  else {
      cout<< "Case #"<<casenum<<": " << number << endl;
    //cout<< "tidy number is :" << number << endl;
    return true;
  }
}

long long dahai_zarb(long long dafa) {
  long long x = 10, result = 1;
  for (long long i = dafa; i > 1; i--)
    result = result * x;
  return result;
}


int main() {



  long long y = 0;
  long long pashi, jawab, modulo;
  bool sahi, galat;
  int a, b;
  cin>>a;
  if (a>0) {
    
    for (int b = 1; b <= a; b++) {
      cin>> y;
     
      //while (infile >> y) {
        sahi = false;
        while (sahi != true) {
          jawab = dahai_jawab(y);
          if (y < 10) {
            cout<< "Case #"<<b<<": " << y << endl;
            break;
          }
          sahi = tidy_number(y, jawab,b);
          if (sahi == true)
            break;
          y--;
        }
      }
    }
      else cout<< "wrong input";


    return 0;
  }
