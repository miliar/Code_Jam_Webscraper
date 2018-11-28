#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

unsigned long long N, copyN, result;
int T;

int main()
{
        int i, j, pos, digits[20], test, aux;
        fin >> T;
        for (test = 1; test <= T; test++) {
                fin >> N;
                copyN = N;
                i = 0;
                while (copyN != 0) {
                        digits[i] = copyN % 10;
                        copyN /= 10;
                        i++;
                }
                pos = i; //number of digits

                for(i=pos-1,j=0; i>=pos/2;i--,j++)
                        swap(digits[i],digits[j]); //reversing vector

                if (pos == 1) {
                        result = N;
                        fout << "Case #" << test << ": " << result << "\n";
                        continue;
                }
                aux=i=0;
                for (i = 0; i < pos-1; i++){
                        if(digits[i] > digits[i+1]) {
                                aux = i;
                                while (digits[aux] > digits[aux+1] && aux!=-1) {
                                        digits[aux]--;
                                        digits[aux+1] = 9;
                                        aux--;
                                }
                                aux=i+1;
                                for(i=aux;i<pos;i++)
                                        digits[i] = 9;
                                break;
                        }
                }
                if(digits[0] == 0) {
                        pos--;
                        for(i=0;i<pos;i++)
                                digits[i] = 9;
                }
                fout << "Case #" << test << ": ";
                for(i=0;i<pos;i++)
                        fout << digits[i];
                fout << "\n";
        }
        fin.close();
        fout.close();
        return 0;
}
