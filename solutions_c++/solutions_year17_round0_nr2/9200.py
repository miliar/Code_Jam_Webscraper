#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <cstring>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


string tidy(string str)
{
int length = str.length();
cout<< length<<endl;
cout<< length;

}
int main() {
  int t;
  string str;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {
    cin >> str;  // read n and then m.

    int length = str.length();
    char * c_str = new char [length +1];
    strcpy (c_str, str.c_str());
    for(int j=0;j<length-1;){

        while((j<(length-1) )&&
              ((c_str[j]-'0') <=
               (c_str[j+1]-'0'))){
            j++;
        }
        if(j == (length -1)) break;
        else{

         c_str[j] = c_str[j] -1;
         for(int temp=j+1;temp<length;temp++)
         c_str[temp] = '9';

        j=j-1;
        if(j<0) j=0;
    //    cout << "Case #" << i << ": "<<c_str << endl;
        }
    }
    int k =0;
for(k=0;k<length-1;k++){ if(c_str[k] == '0') continue; else break;}

    cout << "Case #" << i << ": "<<c_str+k << endl;

  }
}
