#include <fstream>
#include <iostream>
#include <string>

char numToChar(int);

using namespace std;

int main(void)
{
    ifstream input("in.txt");
    ofstream output("out.txt");
    
    string number;
    long longNumber;
    int numCases;
    bool keepGoing = true;
    
    if (input.is_open())
    {
        getline(input, number);
        numCases = stoi(number);
        
        for(int i=0; i<numCases; i++)
        {
            getline(input, number);
            
            if(number.length() == 1)
            {
                cout << "Case #" << i+1 << ": " << number << endl;
                output << "Case #" << i+1 << ": " << number << endl;
                continue;
            }
            else
            {
                longNumber = stol(number);
                
                while(keepGoing == true)
                {
                    number = to_string(longNumber);
                    if(number.length() == 1)
                    {
                        keepGoing = false;
                        break;
                    }
                    
                    for(int j=0; j<number.length()-1; j++)
                    {
                        int firstNum = stoi(string(1, number[j]));
                        int secondNum = stoi(string(1,number[j+1]));
                        
                        if(firstNum > secondNum)
                        {
                            //change firstNum to firstNum - 1
                            //change every number after firstNum to 9
                            //set longnumber equal to that number
                            /*string nines;
                            int numNines = number.length() - (j+1);
                            for(int stuff = 0; stuff < numNines; stuff++)
                            {
                                nines += "9";
                            }
                            number[j] = string(1, (firstNum -1)) + nines;
                            cout << number << endl;
                            return 0;*/
                            number[j] = numToChar(firstNum -1);
                            for(int k = j+1; k < number.length(); k++)
                            {
                                number[k] = '9';
                            }

                            longNumber = stol(number);
                            keepGoing = true;
                            break;
                        }
                        else
                        {
                            keepGoing = false;
                        }
                    }
                    
                    
                }
            
                cout << "Case #" << i+1 << ": " << number << endl;
                output << "Case #" << i+1 << ": " << number << endl;
                keepGoing = true;
            }
        }

        input.close();
        output.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}

char numToChar(int theNumber)
{
    switch(theNumber)
    {
        case 0: return '0';
        case 1: return '1';
        case 2: return '2';
        case 3: return '3';
        case 4: return '4';
        case 5: return '5';
        case 6: return '6';
        case 7: return '7';
        case 8: return '8';
        case 9: return '9';
        default: return '0';
    }
    
}
