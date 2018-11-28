#include <fstream>
using namespace std;
bool isgood(int n)
{
    int k = n;
    if (k < 10){
        return true;
    }
    while(k >= 10 && k % 10 >= (k % 100) / 10){
        k /= 10;
    }
    if (k >= 10 && k % 10 < (k % 100) / 10){
        return false;
    }
    return true;
}
int main()
{
    ifstream fin;
    fin.open("numin.txt");
    int num;
    fin >> num;
    ofstream fout;
    fout.open("numout.txt");
    for (int i = 0; i < num; i++){
        int n;
        fin >> n;
        while(!isgood(n)){
            n--;
        }
        fout << "Case #" << i + 1 << ": " << n << "\n";
    }
}
