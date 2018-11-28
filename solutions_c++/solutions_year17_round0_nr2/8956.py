#include <iostream>
#include <string>

using namespace std;

string tidyify(string tnstr)
{
     int i; //last tidy position
     bool zeroing = false;
     for(i=0; i<tnstr.length(); i++)
     {
          if(zeroing)
               tnstr[i] = '0';
          if(i < tnstr.length()-1 && tnstr[i+1] < tnstr[i])
               zeroing = true;
     }
     
     if(zeroing)
     {
          unsigned long tnp1 = stoul(tnstr);
          tnp1--;
          return tidyify(to_string(tnp1));
     }
     else
          return tnstr;
}

int main()
{
     string cases_;
     getline(cin,cases_);
     int cases = stoi(cases_);

     for(int z=0; z<cases; z++)
     {
          string tnstr;
          getline(cin,tnstr);
          cout << "Case #" << z+1 << ": " << tidyify(tnstr) << endl;
     }
          
     return 0;
}
