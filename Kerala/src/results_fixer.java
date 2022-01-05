import java.io.*;
import java.util.*;
public class results_fixer {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    public static void main(String[] args) throws IOException {
        //Scanner keyboard = new Scanner(System.in);
        FastReader keyboard = new FastReader();
        // pass the file through stdin, fixed file should be generated through redirection (result_fixer < input > output)
        try {
            String str = "";
            while (true) {
             str = keyboard.nextLine();
            if (str.contains("School Code") || str.length() < 4)
            {
                // nothing
            }
            else
            {
                // parse them
                String[] split = str.split(" ");
                // roll no
                System.out.print(split[0] + "|");
                // name
                StringBuilder sb = new StringBuilder();
                int index = 1;
                for (; ; index++)
                {
                    String s = split[index];
                    if (!s.equals("SCIENCE") && !s.equals("COMMERCE") && !s.equals("HUMANITIES") && !s.equals("TECHNICAL"))
                    {
                        // append to name
                        sb.append(s).append(" ");
                    }
                    else {
                        sb.deleteCharAt(sb.length() - 1);
                        break;
                    }
                }
                System.out.print(sb.toString() + "|");
                // stream
                System.out.print(split[index]);
                // handle cases with nonexistient subjects
                if (split[index + 1].equals("")) {
                    System.out.println();
                    continue;
                }
                // each subject
                int subindex = 0;
                StringBuilder sb2 = new StringBuilder();
                ArrayList<String> gradekeywords = new ArrayList<>();
                gradekeywords.add("A+");
                gradekeywords.add("A");
                gradekeywords.add("B+");
                gradekeywords.add("B");
                gradekeywords.add("C+");
                gradekeywords.add("C");
                gradekeywords.add("D+");
                gradekeywords.add("D");
                gradekeywords.add("E");
                gradekeywords.add("F");
                gradekeywords.add(" ");
                gradekeywords.add("Ab");
                for (int i = index + 1; ; i++)
                {
                    if (subindex % 4 == 0)
                    {
                        // append subject till we get a grade or a blank
                        if (!gradekeywords.contains(split[i]))
                        {
                            sb2.append(split[i]);
                            sb2.append(" ");
                        }
                        else
                        {
                            // reset
                            sb2.deleteCharAt(sb2.length() - 1);
                            System.out.print("|" + sb2.toString() + "|" + split[i]);
                            subindex+=2;
                            sb2 = new StringBuilder();
                        }
                    }
                    else {
                        subindex++;
                        System.out.print(split[i]);
                    }
                    if (split[i].equals("NHS") || split[i].equals("EHS") || split[i].equals("RAL")) {
                        // finish up and break, last one there
                        System.out.print("|" + split[i]);
                        System.out.println();
                        break;
                    }
                    else if (subindex % 4 != 0)
                    {
                        System.out.print("|");
                    }
                }
            }
            }
        }
        catch (Exception e) {

        }
    }
}