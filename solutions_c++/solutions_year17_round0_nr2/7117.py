#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
using namespace std;


int main(){

    int ch;
    unsigned long int n,ni,nii,result;
    int flag;
    cin >> ch;

    vector<int> digits;
    for(int caseno=1;caseno<ch+1;caseno++){
        flag=0;
        cin >> n;
        nii=n;
        digits.clear();
        ni=nii;
        while (ni){
            digits.push_back(ni % 10);
            ni /= 10;
        }
        //reverse(digits.begin(),digits.end());
        std::vector<int>::iterator jt;
        for (std::vector<int>::iterator it = digits.begin(); it != digits.end() ; ++it){
            jt = it+1;
            if (jt != digits.end()){
                if(*it < *jt){
                    for(std::vector<int>::iterator pt = digits.begin(); pt <= it ; ++pt){
                        *pt = 9;
                    }
                    *jt = *jt -1;
                }
            }
        }
        reverse(digits.begin(),digits.end());

        result = 0;
        for (std::vector<int>::iterator nt = digits.begin(); nt != digits.end(); ++nt){
            result= result*10+ *nt;
        }
        cout << "Case #" << caseno << ": "<< result << endl;

    }

    return 0;

}
