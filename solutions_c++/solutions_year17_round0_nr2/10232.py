#include <iostream>
#include <fstream>

using namespace std;

bool orde(int);

int main()
{
    ifstream cin("B-small-attempt1.in");
    ofstream cout("out.txt");
    int cases;
    cin >> cases;
    for(int i=1;i<=cases;i++)
    {
        int num;
        cin >> num;
        int num2 = num;
        bool orden = true;
        do
        {
            orden = orde(num2);
            num2--;
        }while(orden);
        cout << "Case #" << i << ": " << num2+1<< endl;
    }
}

bool orde(int n)
{
    int num1 = n%10;
    int num2;
    int auxn = n;
    bool aux = false;
    while(auxn>0)
    {
        auxn/=10;
        num2=auxn%10;
        if(num1<num2)
        {
            aux = true;
        }
        num1=num2;
    }
    return aux;


}
