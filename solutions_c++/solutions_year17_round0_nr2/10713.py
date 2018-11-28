#include <iostream>
#include <string>
#include <sstream>

using namespace std;

template <typename T>
string to_string(T value){

	ostringstream os;
	os << value;
	return os.str();
}

bool verify(unsigned long long numb){

    string tempNumb = to_string(numb);
//cout << tempNumb << endl;
    for(unsigned long long i=0; i<tempNumb.size();i++){
        if(i+1!=tempNumb.size()){
            if(tempNumb[i+1]<tempNumb[i]){
               // cout << "false " << tempNumb[i+1] << "<" <<tempNumb[i] << endl;
                return false;
            }
        }
    }
  //  cout << "true" << endl;
    return true;
}

string calcTidy(unsigned long long maxNumber){

    unsigned long long numb = maxNumber;
    bool tidy=false;

    while(!tidy){
//cout << maxNumber << endl;
        if(!verify(maxNumber)){
            maxNumber--;
        }else{
            tidy = true;
        //    cout << tidy << endl;
        }
    }

    return to_string(maxNumber) ;
}

int main(){

    int testeNumber;
    unsigned long long maxNumber;

    cin >> testeNumber;
    //testeNumber = 1;

    for (int i = 0; i <testeNumber; i++) {

        cin >> maxNumber;
        //maxNumber = 109;
        cout << "Case #" << i+1 << ": " << calcTidy(maxNumber) << endl;

    }

    return 0;
}
