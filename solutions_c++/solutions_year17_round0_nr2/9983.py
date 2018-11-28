#include <fstream>

using namespace std;

//check if number is nondecreasing
//if not then decrement until last digit is satisfied
//repeat steps 1 and 2 for the number excluding the last digit

bool non(string s){
    int k = s.length();
    if (k == 1) 
        return true;
    else
        return non(s.substr(0,k-1)) && (s[k-2] <= s[k-1]); 
}

long f(long n){
    if (non(to_string(n)))
        return n;
    else{
        return f(n/10 - 1)*10 + 9;
    }
}

int main(){
    ifstream fin("B-large.in.txt");
    ofstream fout("B-large.out.txt");
    int n;
    fin >> n;
    for (int i=0; i<n; i++){
    	long temp;
    	fin >> temp;
        long t = f(temp);
        fout << "Case #" << i+1 << ": " << t << "\n";
    }
}