// basic file operations
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;



// write line into output file
void writeLineIntoFile(char * filename,int caseID ,double lastTidy){
  ofstream myfile;
  myfile.open (filename,ofstream::app);
  myfile << "Case #"<<caseID<<": "<<lastTidy<<"\n";
  myfile.close();
}
// string to int
double stringToInt(string intAsString){
double result;
istringstream convert(intAsString);
convert >> result;
return result;
}

string intToString(double number){
stringstream ss;
ss << number;
string str = ss.str();
return str;

}

bool isTidy(string numberAsString){
    int n=numberAsString.size();
    bool boolean=false;
    for(long long  i=0 ;i<n-1;i++){
        boolean= numberAsString[i]>numberAsString[i+1];
        if(boolean){
        return false;
        }
    }
    return true;
}

double lastTidyNumberCounted(string numberAsString){
  double  input =stringToInt(numberAsString);
    for(long long i=input;i>=0;i--){
        if(isTidy(intToString(i))) {
            return i;
        }

    }
    return 0;

}

int main () {



  int i=0;
  ifstream infile("B-small-attempt0.in");
  string line;
  while (getline(infile, line)) {
        if(i!=0){
                  writeLineIntoFile("output.txt",i,lastTidyNumberCounted(line));
        }
        i++;
  }
  return 0;

}
