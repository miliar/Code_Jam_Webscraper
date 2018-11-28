//Design By Robert Jiun-Ting Jiang 20160409
//gcj2016_qualify_pa
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
//#include <deque>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
int string2Int(std::string s){
	  int ii ;
	  std::stringstream ss3; ss3.clear();
	  ss3 << s;
	  ss3 >> ii;
	  return ii;
}
double string2Double(std::string s){
	  double ii ;
	  std::stringstream ss3; ss3.clear();
	  ss3 << s;
	  ss3 >> ii;
	  return ii;
}


std::string Int2string(int i ){
	  std::stringstream ss3; ss3.clear();
	  ss3 << i;
	  std::string ss="";
	  ss3 >> ss;
	  return ss;
}
std::string Double2string(double dd ){
	  std::stringstream ss3; ss3.clear();
	  ss3 << dd;
	  std::string ss="";
	  ss3 >> ss;
	  return ss;
}


int main() {
    int n_testcase, i, j, x, y;
	//int digHash[10];

    cin >> n_testcase;
    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {
        cout << "Case #" << (i_testcase) << ": ";
        int a;;
		cin >>a;
		int ans=0;
		bool IsOk=false ;
		for (int i=a;i>=0 ; i--) {
            string s_i=  Int2string(i);
            char c=0, cmax=0;

            int j;
            for ( j=0;j< s_i.length() ; j++    )  {
                    //cout <<
                    char c=s_i[j];
                    if( j==0) {
                        cmax= c;
                    } else {
                        if (c>= cmax)  {
                            cmax=c;
                        } else {
                            break;
                        }
                    }
            }
            if  (j >= s_i.length()  ) {
                //ok
                IsOk=true;
                ans=i;
                break;
            }
        }
        if ( IsOk==true) {
            cout << ans <<endl;
        }
    }
    return 0;
}
