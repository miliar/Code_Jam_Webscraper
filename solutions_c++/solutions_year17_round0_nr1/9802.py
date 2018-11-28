#include<iostream>
#include<fstream>
#include<string>
using namespace std;



int main()
{

	char currstring[1000];
	
	int k;

	ifstream in;
	ofstream out;

	int count = 0;
	int currsize =0;

	int Case=0;

	int min_num_of_steps=0;

	in.open("A-small-attempt1.in");

	out.open("output.txt");


	int dummy=0;
	if(in.is_open())
	{
		in>>dummy;

		while(!in.eof())
		{

			

			Case++;
			currsize = 0;
			min_num_of_steps=0;

			in>>currstring;
			in>> k;

			

			cout<<currstring;
			
			for (int s = 0; s < currstring[s]!='\0'; s++)
			{
				currsize++;
			}


			for (int i = 0; i < currstring[i]!='\0'; i++)
			{

				int count = 0;
				


				if(currstring[i]=='-')
				{
					min_num_of_steps++;
					int check = i+k;

					if(check>currsize)
					{

						cout<<"Case #"<<Case<<": "<<"IMPOSSIBLE"<<endl;
						out<<"Case #"<<Case<<": "<<"IMPOSSIBLE"<<endl;
						break;

					}

					for (int j = i; j < i+k; j++)
					{

						if(currstring[j]=='-')
							currstring[j] = '+';
						else if(currstring[j]=='+')
							currstring[j] = '-';

					}



				
				}

					for (int c = 0; c < currstring[c]!='\0'; c++)
						{
					
							if(currstring[c] == '+')
							{
								count++;
							}
							
						}

						if(count==currsize)
						{
							cout<<"Case #"<<Case<<": "<<min_num_of_steps<<endl;
							out<<"Case #"<<Case<<": "<<min_num_of_steps<<endl;
							break;
						}


						
			}
			








		}

	}

	out.close();
	in.close();
	


	
	







}