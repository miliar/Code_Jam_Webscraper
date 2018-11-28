#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

#define STRSIZE 256

int main (int argc, char* argv[]) {

	string infile;
	string outfile;
	
	if (argc != 3) {
		printf("Usage: tidy-numbers [infile] [outfile]\n");
		exit(1);
	} else {
		infile = string(argv[1]);
		outfile = string(argv[2]);
	}
	
	int cases;
	vector<string> numbers;
	
	char linebuf_cstr[STRSIZE];
	FILE *infile_ptr = fopen(infile.c_str(), "r");
	int line_num = 1;
	while (fgets(linebuf_cstr, STRSIZE-1, infile_ptr) != NULL) {
	
		string linebuf = string(linebuf_cstr);
		linebuf.erase(linebuf.find_last_not_of(" \n\r\t")+1);
		// int num = atoi(linebuf.c_str());
		
		if (line_num == 1) {
			cases = atoi(linebuf.c_str());
		} else {
			numbers.push_back(linebuf);
		}
		line_num++;
	}
	if (!(feof(infile_ptr)) && ferror(infile_ptr)) { // This is an error
		char preamble[STRSIZE];
		sprintf(preamble, "There was an error reading from %s", infile.c_str());
		perror(preamble);
		return 1;
	}
	fclose(infile_ptr);
	
	vector<string> tidy (cases,"");
	
	for (unsigned int i = 0; i < numbers.size(); i++) {
		
		// Base case
		if (numbers[i].size() == 1) {
			tidy[i] = numbers[i];
			continue;
		}
	
		// Initialize
		string tidy_number = "";
		for (int digits_seen = 1; digits_seen < numbers[i].size(); digits_seen++) {
			char cfirst = numbers[i][digits_seen-1];
			char csecond = numbers[i][digits_seen];
		
			int first = cfirst - '0';
			int second = csecond - '0';
		
			if (first > second) { // Need to do something
				int new_first = first - 1;
				// if (new_first == 0) { // Leading 9s
				string new_tidy_number = "";
			
				char tmp[STRSIZE];
				sprintf(tmp, "%d", new_first);
				new_tidy_number.push_back(tmp[0]);
			
				for (int j = digits_seen-2; j >= 0; j--) {
					char cdfirst = numbers[i][j];
					char cdsecond = new_tidy_number[0];
				
					int dfirst = cdfirst - '0';
					int dsecond = cdsecond - '0';
				
					if (dfirst > dsecond) {
						int new_dfirst = dfirst - 1;
						new_tidy_number[0] = '9';
						
						char tmp2[STRSIZE];
						sprintf(tmp2, "%d", new_dfirst);
						new_tidy_number = string(tmp2) + new_tidy_number;
					} else {
						char tmp2[STRSIZE];
						sprintf(tmp2, "%d", dfirst);
						new_tidy_number = string(tmp2) + new_tidy_number;
					}
				}
				
// 					for (int j = 1; j < digits_seen; j++) {
// 						new_tidy_number.push_back('9');
// 					}
				tidy_number = new_tidy_number;
// 				} else { // Push back the new first onto the tidy number, wrap up tidy number
// 					char tmp[STRSIZE];
// 					sprintf(tmp, "%d", new_first);
// 					tidy_number.push_back(tmp[0]);
// 				}
				for (int j = digits_seen; j < numbers[i].size(); j++) {
					tidy_number.push_back('9');
				}
				break;
			} else { // Push back the first onto the tidy_number, continue
				tidy_number.push_back(cfirst);
				if (digits_seen+1 == numbers[i].size()) { // Fencepost
					tidy_number.push_back(csecond);
				}
			}
		}
		
		// Clean up leading zeroes
		if (tidy_number[0] == '0') {
			tidy_number.erase(0,1);
		}
		
		tidy[i] = tidy_number;
	}
	
	// Print the output
	FILE *outfile_ptr = fopen(outfile.c_str(), "w");
	for (unsigned int i = 0; i < tidy.size(); i++) {
		fprintf(outfile_ptr, "Case #%d: %s\n", i+1, tidy[i].c_str());
	}
	fclose(outfile_ptr);
	return 0;
}
