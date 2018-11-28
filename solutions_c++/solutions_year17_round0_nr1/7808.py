#include<iostream>
#include<fstream>
#include<cstdlib>
#include <algorithm>
#include <string.h>

using namespace std;


#include <stdlib.h>
#include <stdio.h>

     

    void do_flip(int *, int, int);

     

    /*Function to implement the pancake sort*/

    int pancake_sort(int *list, unsigned int length)

    {

        if (length < 2)

            return 0;

        int i, a, max_num_pos, moves;

     

        moves = 0;

        for (i = length;i > 1;i--)

        {

            max_num_pos = 0;

            for (a = 0;a < i;a++)

            {

                if (list[a] > list[max_num_pos])

                    max_num_pos = a;

            }

            if (max_num_pos ==  i - 1)

                continue;

            if (max_num_pos)

            {

                moves++;

                do_flip(list, length, max_num_pos + 1);

            }

            do_flip(list, length, i);

        }

        return moves;

    }

     

    /*Function to do flips in the elements*/

    void do_flip(int *list,  int length,  int num)

    {

        int swap;

        int i = 0;

        for (i;i < --num;i++)

        {

            swap = list[i];

            list[i] = list[num];

            list[num] = swap;

        }

    }

     

    /*Function to print the array*/

    void print_array(int list[], int length)

    {

        int i;

        for (i = 0;i < length;i++)

        {

            printf("%d ", list[i]);

        }

    }




int main(){
	std::ifstream infile("A-large.in");
	int t, p, l;
	infile >> t;
	string sentence = "";
//	getline(infile, sentence, ' ');
//		cout<<endl<<sentence<<endl;
	for(l=0;l<t;l++){
		getline(infile, sentence, ' ');
	//	cout<<endl<<sentence<<endl;
		infile >> p;
		int i = 0;
		int count = 0;
		int rt = 0;
		int moves = 0;
		while(sentence[i]!='\0'){
			rt++;
			i++;
		}
		i = 0;
		int list[rt];
		for(int sy = 0; sy<rt; sy++){
			if(sentence[sy]=='+'){
				list[sy] = 1;
			} else
				list[sy] = 0;
		}
		while(sentence[i]!='\0') {
			if(sentence[i] == '-' && i <= rt - p) {
				for(int s = i; s < i+p; s++){
					if(sentence[s] == '-')
						sentence[s] = '+';
					else
						sentence[s] = '-';
				}
			//	cout<<endl<<sentence<<endl;
				count++;
			}
			i++;
		}
		int iset = 1;
		for(int st = 0; sentence[st]!='\0';st++){
			if(sentence[st]=='-') {
				iset = 0;
				cout<<"Case #"<<l+1<<": IMPOSSIBLE"<<endl;
				break;
			}
		}
		if(iset == 1) {
			moves  =  pancake_sort(list, rt);
			cout<<"Case #"<<l+1<<": "<<count<<endl;
		}
//		cout<<count;
	}	
	return 0;
}
