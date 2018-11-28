#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
bool checkTidy(int number)
{
    int num_arr[20]={},k=0,j=0,last_num;
    while(number)
    {
        //cout << number%10 << endl;
        num_arr[k] = number%10;
        number /= 10;
        k++;
    }
    bool is_tidy = true;
    last_num = num_arr[0];
    //cout << last_num << endl;
    for( j=1;j<(k);j++ )
    {
        //cout << num_arr[j] << endl;
        if( last_num < num_arr[j] ) {
            is_tidy = false;
            break;
        }
        last_num = num_arr[j];
    }
    return is_tidy;
}
int isTidyNumber(int number )
{
    int tidy_number;
    bool is_continue = true,is_tidy=false;
    while(is_continue)
    {
        is_tidy = checkTidy(number);
        if( is_tidy ) {
          break;
        } else {
           number--;
        }
    }
    return number;
}

int main() {
  freopen("B-small-attempt1.in", "r", stdin);
  freopen("B-small-attempt1.out", "w", stdout);
  int t, n;
  bool is_tidy=0;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    is_tidy = isTidyNumber(n);
    cout << "Case #" << i << ": " << isTidyNumber(n) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
